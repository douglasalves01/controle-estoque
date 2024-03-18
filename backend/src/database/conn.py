import oracledb
import os
from dotenv import load_dotenv

load_dotenv()
DB_USER=os.getenv('USER_ORACLE_CONNECTION')
DB_PASSWORD=os.getenv('PASSWORD_ORACLE_CONNECTION')
DB_STRING=os.getenv('STRING_ORACLE_CONNECTION')

def conn():
    try:
        connection = oracledb.connect(
            user=DB_USER,
            password=DB_PASSWORD,
            dsn=DB_STRING)  

        print("Conectado no banco de dados com sucesso")
        return connection

    except Exception as e:
        print("Ocorreu um erro: ", e)
        return None
    
