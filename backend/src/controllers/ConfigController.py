from database.conn import conn
from oracledb import DatabaseError
from fastapi import HTTPException

class ConfigController:
    connection = conn()
    cursor = connection.cursor()

    @staticmethod
    def configSave(margem_lucro,comissao_venda,custo_fixo, imposto,id):
        print(margem_lucro)
        print(comissao_venda)
        print(custo_fixo)
        print(imposto)
        print(id)
        try:
            
            if(margem_lucro is None or margem_lucro==""):
                raise HTTPException(status_code=422, detail="Insira a margem de lucro!")
            if(comissao_venda is None or comissao_venda==""):
                raise HTTPException(status_code=422, detail="Insira a comissão de venda!")
            if(custo_fixo is None or custo_fixo==""):
                raise HTTPException(status_code=422, detail="Insira o custo fixo!")
            if(imposto is None or imposto==""):
                raise HTTPException(status_code=422, detail="Insira o imposto!")
            ConfigController.cursor.execute("UPDATE TBLCONFIG SET MARGEM_LUCRO=:1, COMISSAO_VENDA=:2,CUSTO_FIXO=:3,IMPOSTO_VENDA=:4 WHERE ID=:5", [margem_lucro,comissao_venda,custo_fixo,imposto,id])
            ConfigController.connection.commit()  
            print(ConfigController.cursor.rowcount, "Rows Inserted")
        except DatabaseError as e:
            raise HTTPException(status_code=500, detail="Erro ao inserir configurações no banco de dados: " + str(e))
    
    #método para retornar todas as categorias    
    @staticmethod
    def getAllConfig():
        try:
            ConfigController.cursor.execute("select * from tblconfig")
            rows = ConfigController.cursor.fetchall()
            return rows
        except DatabaseError as e:
            raise HTTPException(status_code=500, detail="Erro ao retornar conigurações do banco de dados: " + str(e))
    