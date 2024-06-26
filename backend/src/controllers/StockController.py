from helpers.get_user_by_token import getUserByToken
from database.conn import conn
from oracledb import DatabaseError
from fastapi import HTTPException, Request
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from helpers.create_access_token import create_access_token
from datetime import datetime, timedelta, timezone
import os
from dotenv import load_dotenv

class StockController:
    load_dotenv()
    connection=conn()
    cursor=connection.cursor()
    
    @staticmethod
    async def Movimentacao(quantidade:int,id_product:int,motivo_transacao:str,custo_unitario:float,typeMoviment:str,request:Request):
        try:
            data_atual=datetime.now()
            ##pegar usuário logado
            user=getUserByToken(request)
            StockController.cursor.execute("select id from tblusuario where nome=:1", [user])
            id_user=StockController.cursor.fetchone()[0]
            
            ##inserindo movimentação no banco
            StockController.cursor.execute("INSERT INTO TBLCONTROLEESTOQUE (TIPO_TRANSACAO,DATA_HORA_TRANSACAO,MOTIVO_TRANSACAO,ID_USUARIO,ID_PRODUTO,QUANTIDADE,CUSTO_UNITARIO) VALUES (:1,:2,:3,:4,:5,:6,:7)",[typeMoviment,data_atual,motivo_transacao,id_user,id_product,quantidade,custo_unitario])
            StockController.connection.commit()  
            print(StockController.cursor.rowcount, "Rows Inserted")
        except DatabaseError as e:
            raise HTTPException(status_code=500, detail="Erro ao realizar movimento! Tente novamente mais tarde!: " + str(e))
    