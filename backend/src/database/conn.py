import oracledb
import os
from dotenv import load_dotenv
import requests
from oracledb import DatabaseError

#Desabilitando a verificação SSL para a próxima requisição
response = requests.get('http://127.0.0.1:8000', verify=False)

#Verificar se a requisição foi bem-sucedida
if response.status_code == 200:
  print("Requisição bem-sucedida!")
  print("Conteúdo da resposta:", response.text)
else:
  print("Erro na requisição:", response.status_code)


load_dotenv()
DB_USER=os.getenv('USER_ORACLE_CONNECTION')
DB_PASSWORD=os.getenv('PASSWORD_ORACLE_CONNECTION')
DB_STRING=os.getenv('STRING_ORACLE_CONNECTION')

def conn():
    try:
        connection = oracledb.connect(
            user=DB_USER,
            password=DB_PASSWORD,
            dsn=DB_STRING,
            ssl_server_cert_dn= True
            )
            

        print("Conectado no banco de dados com sucesso")
        return connection

    except Exception as e:
        print("Ocorreu um erro: ", e)
        return None