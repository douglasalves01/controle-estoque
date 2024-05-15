from database.conn import conn
from oracledb import DatabaseError
from fastapi import HTTPException, Request
from datetime import datetime
from helpers.get_user_by_token import getUserByToken
from dotenv import load_dotenv

class ProductController:
    load_dotenv()
    connection=conn()
    cursor=connection.cursor()

    @staticmethod
    def createProduct(product,price,unit_measure,id_supplier,id_category,currentStock,minimumStock,unitCost,location,description,icms,request:Request ):
        try: 
            data_atual = datetime.now()
            status='ativo'
            print(currentStock)
            print(minimumStock)
            print(unitCost)
            #verificar se os campos necessários vieram nulos ou vzios
            if(product is None or product==""):
                raise HTTPException(status_code=422, detail="Insira o nome do produto!")
            if(price is None or price==""):
                raise HTTPException(status_code=422,detail="Insira o valor do produto!")
            if(status is None or status==""):
                raise HTTPException(status_code=422,detail="Insira o status do produto!")
            if(description is None or description==""):
                raise HTTPException(status_code=422,detail="Insira a descrição do produto!")
            if(icms is None or icms==""):
                raise HTTPException(status_code=422,detail="Insira o ICMS do produto!")
            if(unit_measure is None or unit_measure==""):
                raise HTTPException(status_code=422,detail="Insira a unidade de medida do produto!")
            if(minimumStock is None or minimumStock==""):
                raise HTTPException(status_code=422,detail="Insira o estoque mínimo do produto!")
            if(id_category is None or id_category ==""):
                raise HTTPException(status_code=422,detail="insira a categoria do produto!")
            if(id_supplier is None or id_supplier==""):
                raise HTTPException(status_code=422,detail="Insira o fornecedor para o produto!")
            if(unitCost is None or unitCost==""):
                raise HTTPException(status_code=422,detail="Insira o custo unitário produto!")
            if(location is None or location ==""):
                raise HTTPException(status_code=422,detail="insira a localização do produto!")
            if(currentStock is None or currentStock ==""):
                raise HTTPException(status_code=422,detail="insira a quantidade do produto!")
            
            #verificar se já existe um produto igual cadastrado
            ProductController.cursor.execute("select * from tblproduto where produto= :1",[product])
            rows=ProductController.cursor.fetchall()
            
            if(rows):
                raise HTTPException(status_code=422, detail="Produto já existe no banco de dados!")
            
            #inserindo produto
            ProductController.cursor.execute("INSERT INTO tblproduto (produto,valor,status,unidade_medida,id_fornecedor,id_categoria,descricao,icms) VALUES (:1,:2,:3,:4,:5,:6,:7,:8)", [product,price,status,unit_measure,id_supplier,id_category,description,icms]) 
            ProductController.connection.commit()  
            ##INSERIR ESTOQUE
            ##buscar id do produto
            ProductController.cursor.execute("SELECT id FROM tblproduto WHERE produto = :1", [product])
            id_product = ProductController.cursor.fetchone()
            ##inserir o estoque
            ProductController.cursor.execute("INSERT INTO tblestoque (estoque_atual,estoque_minimo,localizacao,custo_unitario,data_ultima_atualizacao,id_produto) VALUES (:1,:2,:3,:4,:5,:6)", [0,minimumStock,location,unitCost,data_atual,id_product[0]]) 
            ProductController.connection.commit()  
            print(ProductController.cursor.rowcount, "Rows Inserted")

            ##pegar usuário logado
            user=getUserByToken(request)
            ProductController.cursor.execute("select id from tblusuario where nome=:1", [user])
            id_user=ProductController.cursor.fetchone()[0]
            ##INSERIR O CONTROLE DO ESTOQUE
            tipo="entrada"
            motivo="entrada de produto no estoque"
            ProductController.cursor.execute("INSERT INTO tblcontroleestoque (tipo_transacao,data_hora_transacao,motivo_transacao,id_usuario,id_produto,quantidade,custo_unitario) values (:1,:2,:3,:4,:5,:6,:7)",[tipo,data_atual,motivo,id_user,id_product[0],currentStock,unitCost])
            ProductController.connection.commit()  
            print(ProductController.cursor.rowcount, "Rows Inserted")
        except DatabaseError as e:
            raise HTTPException(status_code=500, detail="Erro ao inserir produto no banco de dados: " + str(e))
        
    @staticmethod
    def updateProduct(product,price,status,unit_measure,id_supplier,id_category,id_product):
        try:
            #verificar se os campos necessários vieram nulos ou vazios
            if(product is None or product==""):
                raise HTTPException(status_code=422, detail="Insira o nome do produto!")
            if(price is None or price==""):
                raise HTTPException(status_code=422,detail="Insira o valor do produto!")
            if(status is None or status==""):
                raise HTTPException(status_code=422,detail="Insira o status do produto!")
            if(unit_measure is None or unit_measure==""):
                raise HTTPException(status_code=422,detail="Insira a unidade de medida do produto!")
            if(id_supplier is None or id_supplier==""):
                raise HTTPException(status_code=422,detail="Insira o fornecedor para o produto!")
            if(id_category is None or id_category ==""):
                raise HTTPException(status_code=422,detail="insira a categoria do produto!")
           
            ProductController.cursor.execute("UPDATE tblproduto SET produto = :1, valor = :2, status = :3, unidade_medida = :4, id_fornecedor = :5, id_categoria = :6 WHERE id = :7", [product, price, status, unit_measure, id_supplier, id_category, id_product])            
            ProductController.connection.commit()  
            print(ProductController.cursor.rowcount, "Rows Inserted")
        except DatabaseError as e:
            raise HTTPException(status_code=500, detail="Erro ao editar produto no banco de dados: " + str(e))
    
    @staticmethod
    def getAllProducts():
        try:
            ProductController.cursor.execute("select p.id,p.produto,p.valor,p.status,p.unidade_medida,f.nome_fantasia,c.categoria,p.descricao,p.icms from tblproduto p,tblcategoria c,tblfornecedor f where p.id_categoria=c.id and p.id_fornecedor=f.id")
            rows = ProductController.cursor.fetchall()
            return rows
        except DatabaseError as e:
            raise HTTPException(status_code=500, detail="Erro ao retornar produtos do banco de dados: " + str(e))
        
    @staticmethod
    def getAllProductsActive():
        try:
            ProductController.cursor.execute("select * from tblproduto where status='ativo'")
            rows = ProductController.cursor.fetchall()
            return rows
        except DatabaseError as e:
            raise HTTPException(status_code=500, detail="Erro ao retornar produtos do banco de dados: " + str(e))
        
    @staticmethod
    def deleteProduct(id_product):
        try:
            status='inativo'
            ProductController.cursor.execute("UPDATE tblproduto SET status=:1 where id = :2",[status,id_product])
            ProductController.connection.commit()
        except DatabaseError as e:
            raise HTTPException(status_code=500, detail="Erro ao excluir produto do banco de dados: " + str(e))