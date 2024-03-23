from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.security import HTTPBearer
from fastapi import Request
from helpers.get_token import get_token
from jose import JWTError, jwt
import os
from dotenv import load_dotenv
load_dotenv()
security = HTTPBearer()
SECRET_KEY =os.getenv('SECRET_KEY')
ALGORITHM =os.getenv('ALGORITHM')
def getUserByToken(request:Request):
    try:
        token =get_token(request)
     
        if not token:
            raise HTTPException(status_code=401, detail="Acesso negado!")
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        if not payload:
            raise HTTPException(status_code=422, detail="Acesso negado!")
        return payload['sub']
        #veirificar se o token é válido
    except Exception as e:
        raise HTTPException(status_code=422,detail=str(e))
    