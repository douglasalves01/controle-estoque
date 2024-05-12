from database.conn import conn
from oracledb import DatabaseError
from fastapi import HTTPException

class SupplierController:
    connection = conn()
    cursor = connection.cursor()

    @staticmethod
    def createSupplier(cnpj, razao_social, nome_fantasia, endereco, telefone,status):
        try:
            if(cnpj is None or cnpj==""):
                raise HTTPException(status_code=422, detail="Insira o CNPJ!")
            if(razao_social is None or razao_social==""):
                raise HTTPException(status_code=422, detail="Insira a razão social!")
            if(nome_fantasia is None or nome_fantasia==""):
                raise HTTPException(status_code=422, detail="Insira o nome fantasia do fornecedor!")
            if(endereco is None or endereco==""):
                raise HTTPException(status_code=422, detail="Insira o endeço do fornecedor!")
            if(telefone is None or telefone==""):
                raise HTTPException(status_code=422, detail="Insira o telefone do fornecedor!")


            SupplierController.cursor.execute("SELECT * FROM tblfornecedor WHERE cnpj = :1", [cnpj])
            rows = SupplierController.cursor.fetchall()
            if rows:
                raise HTTPException(status_code=422, detail="Este nome de fornecedor já está cadastrado!")

            ##salvar os telefones na tabela telefone com o id do fornecedor cadastrado(usar for)
            SupplierController.cursor.execute("INSERT INTO tblfornecedor (cnpj, razao_social, nome_fantasia, endereco,status) VALUES (:1, :2, :3, :4,:5)", [cnpj,razao_social,nome_fantasia,endereco,status]) 
            SupplierController.connection.commit()  
            SupplierController.cursor.execute("SELECT id FROM tblfornecedor WHERE cnpj = :1", [cnpj])
            id = SupplierController.cursor.fetchone()
            for i in telefone:
                SupplierController.cursor.execute("INSERT INTO tbltelefone (telefone, id_fornecedor) VALUES (:1, :2)", [i,id[0]]) 
                SupplierController.connection.commit() 
        except DatabaseError as e:
            raise HTTPException(status_code=500, detail="Erro ao inserir fornecedor no banco de dados: " + str(e))

    @staticmethod
    def getAllSuppliers():
        try:
            SupplierController.cursor.execute("SELECT * FROM tblfornecedor")
            rows = SupplierController.cursor.fetchall()
            return rows
        except DatabaseError as e:
            raise HTTPException(status_code=500, detail="Erro ao retornar fornecedores do banco de dados: " + str(e))
        
    @staticmethod
    def getAllSuppliersActive():
        try:
            SupplierController.cursor.execute("SELECT * FROM tblfornecedor where status='ativo'")
            rows = SupplierController.cursor.fetchall()
            return rows
        except DatabaseError as e:
            raise HTTPException(status_code=500, detail="Erro ao retornar fornecedores do banco de dados: " + str(e))
        
    @staticmethod
    def updateSupplier(id,cnpj, razao_social, nome_fantasia, endereco, telefone,status):
        try:
            if(cnpj is None or cnpj==""):
                raise HTTPException(status_code=422, detail="Insira o CNPJ!")
            if(razao_social is None or razao_social==""):
                raise HTTPException(status_code=422, detail="Insira a razão social!")
            if(nome_fantasia is None or nome_fantasia==""):
                raise HTTPException(status_code=422, detail="Insira o nome fantasia do fornecedor!")
            if(endereco is None or endereco==""):
                raise HTTPException(status_code=422, detail="Insira o endeço do fornecedor!")
            if(telefone is None or telefone==""):
                raise HTTPException(status_code=422, detail="Insira o telefone do fornecedor!")
   
            if(status is None or status==""):
                raise HTTPException(status_code=422, detail="Insira o status do fornecedor!")
   
            SupplierController.cursor.execute("UPDATE tblfornecedor SET nome = :1, cnpj = :2, razao_social = :3, nome_fantasia = :4, endereco = :5, telefone = :6 WHERE id = :7", 
                                              [ cnpj, razao_social, nome_fantasia, endereco, telefone, id])
            SupplierController.connection.commit()
            
        except DatabaseError as e:
            raise HTTPException(status_code=500, detail="Erro ao atualizar fornecedor no banco de dados: " + str(e))
        
    @staticmethod
    def deleteSupplier(id):
        status="inativo"
        try:
            SupplierController.cursor.execute("UPDATE tblfornecedor SET status= :1 where id=:2", [status,id])
            SupplierController.connection.commit()
            
        except DatabaseError as e:
            raise HTTPException(status_code=500, detail="Erro ao excluir fornecedor do banco de dados: " + str(e))