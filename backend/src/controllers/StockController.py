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

class StockController:
    load_dotenv()
    connection=conn()
    cursor=connection.cursor()
    