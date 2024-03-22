from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from fastapi import Request
from helpers.get_token import get_token
from jose import JWTError, jwt
import os
from dotenv import load_dotenv
load_dotenv()
security = HTTPBearer()
SECRET_KEY =os.getenv('SECRET_KEY')
ALGORITHM =os.getenv('ALGORITHM')
def checkToken(request:Request):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Acesso negado!",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        token =get_token(request)
     
        if not token:
            raise HTTPException(status_code=401, detail="Acesso negado!")
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        if not payload:
            raise HTTPException(status_code=422, detail="Categoria já existe no banco de dados!")
        return payload
        #veirificar se o token é válido
    except JWTError:
        raise credentials_exception
    