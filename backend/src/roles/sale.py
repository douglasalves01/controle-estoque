#VALIDAÇÃO DE ESTOQUE MÍNIMO: Não permitir que uma venda seja concluída se o estoque 
#disponível do produto estiver abaixo de um determinado limite mínimo.
from fastapi import Depends, Request
from database.conn import conn
from fastapi import HTTPException
from oracledb import DatabaseError
from fastapi import HTTPException
from jose import JWTError, jwt
import os
from dotenv import load_dotenv
from fastapi import Request
from typing import List
#admin = tudo liberado
#editor = cadastro/editar/excluir liberado 
#estoque = movimentações/relatórios/estoque
#supervisor = tudo liberado, menos a parte de criar usuário
class saleRoles:
    load_dotenv()
    SECRET_KEY = os.getenv('SECRET_KEY')
    ALGORITHM = os.getenv('ALGORITHM')
    async def checkMinimumStock(produtos:List[str], quantidades:List[int]):
        connection = conn()
        cursor = connection.cursor()
        try:
            for i in range(len(produtos)):
                produto=produtos[i]
                quantidade=quantidades[i]
                cursor.execute("select e.estoque_atual,e.estoque_minimo,p.produto from tblestoque e, tblproduto p where e.id_produto=:1 and p.id=:2", [produto,produto])
                estoque=cursor.fetchone()
                if ((estoque[0]-estoque[1]) <= int(quantidade)):
                    raise HTTPException(status_code=401, detail=f"Quantidade do produto {estoque[2]} desejada insuficiente!")
        except DatabaseError as e:
                raise HTTPException(status_code=500, detail="Erro ao fazer login: " + str(e))
    
         
  