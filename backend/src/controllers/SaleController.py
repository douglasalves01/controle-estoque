from helpers.get_user_by_token import getUserByToken
from database.conn import conn
from oracledb import DatabaseError
from fastapi import HTTPException, Request
from datetime import datetime
from roles.sale import saleRoles
class SaleController:
    connection = conn()
    cursor = connection.cursor()
    @staticmethod
    async def Sale(id_produto,quantidade,request:Request):
        try:
            print(id_produto)
            print(quantidade)
            data_atual = datetime.now()
            valor=0
            if(id_produto is None):
                raise HTTPException(status_code=422,detail="Insira o produto no carrinho!")
            if(quantidade is None):
                raise HTTPException(status_code=422,detail="Insira a quantidade do produto!")
            ##pegar usuário logado
            
            user=getUserByToken(request)
            SaleController.cursor.execute("select id from tblusuario where nome=:1", [user])
            id_user=SaleController.cursor.fetchone()[0]
            ##verificar regra de negócio com a quantidade de estoque
      
            await saleRoles.checkMinimumStock(id_produto,quantidade)
        
            for i in range(len(id_produto)):
                produto=id_produto[i]
                quantidade_produto=quantidade[i]
                SaleController.cursor.execute("select valor from tblproduto where id=:1", [produto])
                valor_unit=SaleController.cursor.fetchone()[0]
                valor+=(float(quantidade_produto)*float(valor_unit))

            SaleController.cursor.execute("INSERT INTO TBLVENDA (DATA,ID_USUARIO,VALOR) VALUES (:1,:2,:3)",[data_atual,id_user,valor])
            SaleController.connection.commit()  
            print(SaleController.cursor.rowcount, "Rows Inserted")
            ##pegando id da ultima venda
            SaleController.cursor.execute("SELECT ISEQ$$_132614.CURRVAL FROM tblvenda")
            id_venda=SaleController.cursor.fetchone()[0]

            ##salvar os itens da venda
            for i in range(len(id_produto)):
                produto=id_produto[i]
                quantidade_produto=quantidade[i]
                SaleController.cursor.execute("INSERT INTO TBLVENDAITEM (QUANTIDADE,ID_PRODUTO,ID_VENDA) VALUES (:1,:2,:3)",[quantidade_produto,produto,id_venda]) 
                SaleController.connection.commit()  
                print(SaleController.cursor.rowcount, "Rows Inserted") 
            
            ##salvar as movimentações no controle de estoque como saída
            tipo_transacao="saida"
            motivo_transacao="venda"
            
            for i in range(len(id_produto)):
                produto=id_produto[i]
                quantidade_produto=quantidade[i]
                SaleController.cursor.execute("select e.custo_unitario from tblestoque e where e.id_produto=:1", [produto])
                custo_unitario=SaleController.cursor.fetchone()[0]
                SaleController.cursor.execute("INSERT INTO TBLCONTROLEESTOQUE (TIPO_TRANSACAO,DATA_HORA_TRANSACAO,MOTIVO_TRANSACAO,ID_USUARIO,ID_PRODUTO,QUANTIDADE,CUSTO_UNITARIO) VALUES (:1,:2,:3,:4,:5,:6,:7)",[tipo_transacao,data_atual,motivo_transacao,id_user,produto,quantidade_produto,custo_unitario]) 
                SaleController.connection.commit()  
                print(SaleController.cursor.rowcount, "Rows Inserted") 
                 
        except DatabaseError as e:
            raise HTTPException(status_code=500, detail="Erro ao realizar venda! Tente novamente mais tarde!: " + str(e))
    