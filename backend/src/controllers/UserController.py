from database.conn import conn
from oracledb import DatabaseError
from fastapi import HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from helpers.create_access_token import create_access_token
from datetime import datetime, timedelta, timezone
import os
from dotenv import load_dotenv

class UserController:
    load_dotenv()
    connection = conn()
    cursor = connection.cursor()
    
    @staticmethod
    def login(name,password):
    #login
        try:
            ACCESS_TOKEN_EXPIRE_MINUTES =os.getenv('ACCESS_TOKEN_EXPIRE_MINUTES')
            pwd_context=CryptContext(schemes=['bcrypt'])
            #verificar se a name veio vazio
            if(name is None or name==""):
                raise HTTPException(status_code=422, detail="Insira o nome!")
            #verificar se password veio vazia
            if(password is None or password==""):
                raise HTTPException(status_code=422, detail="Insira a senha!")
            #verificar se existe o user no banco e retonar o hahs dele
            UserController.cursor.execute("select * from tblusuario where nome = :1",[name])
            resultName=UserController.cursor.fetchone()

            if not resultName:
                raise HTTPException(status_code=422, detail="Digite outro usuário!")
            hashed_senha = resultName[2]        

            resultVerify=pwd_context.verify(password,hashed_senha)
           
            if not resultVerify:
                raise HTTPException(status_code=421, detail="Senha inválida!") 
                          
            access_token_expires = timedelta(minutes=float(ACCESS_TOKEN_EXPIRE_MINUTES))
            access_token = create_access_token(data={"sub": name}, expires_delta=access_token_expires)
            return access_token
            #validar a senha digitada com o hahs do banco
        except DatabaseError as e:
            raise HTTPException(status_code=500, detail="Erro ao fazer login: " + str(e))
        
    @staticmethod
    def register(name, password,id_nivelacesso):
        try:
            #verificar se a name veio vazio
            pwd_context=CryptContext(schemes=['bcrypt'])
            if(name is None or name==""):
                raise HTTPException(status_code=422, detail="Insira o nome!")
            #verificar se password veio vazia
            if(password is None or password==""):
                raise HTTPException(status_code=422, detail="Insira a senha!")
            UserController.cursor.execute("select * from tblusuario where nome = (:1)",[name])
            rows = UserController.cursor.fetchall()
            if(rows):
                raise HTTPException(status_code=422, detail="Usuário já existe no banco de dados!")
            #gerando hashed de senha
            hashed_senha=pwd_context.hash(password)
            #Inserir usuário no banco de dados
            UserController.cursor.execute("INSERT INTO TBLUSUARIO (NOME,SENHA,ID_NIVELACESSO) VALUES (:1,:2,:3)", [name,hashed_senha,id_nivelacesso]) 
            UserController.connection.commit()  
            print(UserController.cursor.rowcount, "Rows Inserted")
        
        except DatabaseError as e:
            raise HTTPException(status_code=500, detail="Erro ao cadastrar novo usuário no banco de dados: " + str(e))
        