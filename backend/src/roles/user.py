from fastapi import Depends, Request
from database.conn import conn
from fastapi import HTTPException
from oracledb import DatabaseError
from fastapi import HTTPException
from jose import JWTError, jwt
import os
from dotenv import load_dotenv
from fastapi import Request

#admin = tudo liberado
#editor = cadastro/editar/excluir liberado 
#estoque = movimentações/relatórios/estoque
#supervisor = tudo liberado, menos a parte de criar usuário
class SimpleAuthBackend:
    load_dotenv()

    SECRET_KEY = os.getenv('SECRET_KEY')
    ALGORITHM = os.getenv('ALGORITHM')
    async def authenticate(self, request: Request):
        

        try:
            if request.headers.get("Authorization"):
                token = request.headers.get("Authorization").split(' ')[1]
                payload = jwt.decode(token, SimpleAuthBackend.SECRET_KEY, algorithms=[SimpleAuthBackend.ALGORITHM])
                return payload
            else:
                raise HTTPException(status_code=401, detail="Acesso negado! Token de autorização não fornecido.")
        except (JWTError, IndexError, AttributeError) as e:
            raise HTTPException(status_code=401, detail="Acesso negado! Token de autorização inválido.")
    
    def verifyAccess(self,request:Request,nivel_description:str):
        #vou receber o nivel do usuario e a descração do nivel
        try:
          
            connection = conn()
            cursor = connection.cursor()
            token = request.headers.get("Authorization").split(' ')[1]
            print(token)
            user = jwt.decode(token, SimpleAuthBackend.SECRET_KEY, algorithms=[SimpleAuthBackend.ALGORITHM])['sub']
            print(user)
            cursor.execute("select n.nome from tblnivelacesso n,tblusuario u where u.nome = :1 and n.id = u.id_nivelacesso",[user] )
            result = cursor.fetchone()[0]
            if(nivel_description=='admin'):
                if not result =='admin':
                    raise HTTPException(status_code=401, detail="Você não tem acesso para realizar essa operação! Contacte o administrador dos sistema!")
                return True
            elif(nivel_description=='editor'):
                if(result=='estoque'):
                    raise HTTPException(status_code=401, detail="Você não tem acesso para realizar essa operação! Contacte o administrador dos sistema!")
                return True
            elif(nivel_description=="estoque"):
                if(result=='editor'):
                    raise HTTPException(status_code=401, detail="Você não tem acesso para realizar essa operação! Contacte o administrador dos sistema!")
                return True
            elif(nivel_description=='supervisor'):
                if(result=='editor' or result=='estoque'):
                    raise HTTPException(status_code=401, detail="Você não tem acesso para realizar essa operação! Contacte o administrador dos sistema!")
                return True
            return True
        except DatabaseError as e:
                raise HTTPException(status_code=500, detail="Erro ao fazer login: " + str(e))
        except (JWTError, IndexError, AttributeError) as e:
            raise HTTPException(status_code=401, detail=e,)
            
  