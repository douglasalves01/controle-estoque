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

class ProductController:
    load_dotenv()
    connection=conn()
    cursor=connection.cursor()

    @staticmethod
    def createProduct(product,price,status,unit_measure,id_supplier,id_category):
        try:
            #verificar se os campos necessários vieram nulos ou vzios
            if(product is None or product==""):
                raise HTTPException(status_code=422, detail="Insira o nome do produto!")
            if(price is None or price==""):
                raise HTTPException(status_code=422,detail="Insira o valor do produto!")
            if(status is None or status==""):
                raise HTTPException(status_code=422,detail="Insira o status do produto!")
            if(unit_measure is None or unit_measure==""):
                raise HTTPException(status_code=422,detail="Insira a unidade de medida do produto!")
            if(id_supplier is None or id_supplier==""):
                raise HTTPException(status_code=422,detail="Insira o fornecedor para o produto!")
            if(id_category is None or id_category ==""):
                raise HTTPException(status_code=422,detail="insira a categoria do produto!")
            
            ProductController.cursor.execute("select * from tblproduto where produto= :1",[product])
            rows=ProductController.cursor.fetchall()
            
            if(rows):
                raise HTTPException(status_code=422, detail="Produto já existe no banco de dados!")
            ProductController.cursor.execute("INSERT INTO tblproduto (produto,valor,status,unidade_medida,id_fornecedor,id_categoria) VALUES (:1,:2,:3,:4,:5,:6)", [product,price,status,unit_measure,id_supplier,id_category]) 
            ProductController.connection.commit()  
            print(ProductController.cursor.rowcount, "Rows Inserted")
        except DatabaseError as e:
            raise HTTPException(status_code=500, detail="Erro ao inserir produto no banco de dados: " + str(e))
        
    @staticmethod
    def updateProduct(product,price,status,unit_measure,id_supplier,id_category,id_product):
        try:
            #verificar se os campos necessários vieram nulos ou vazios
            if(product is None or product==""):
                raise HTTPException(status_code=422, detail="Insira o nome do produto!")
            if(price is None or price==""):
                raise HTTPException(status_code=422,detail="Insira o valor do produto!")
            if(status is None or status==""):
                raise HTTPException(status_code=422,detail="Insira o status do produto!")
            if(unit_measure is None or unit_measure==""):
                raise HTTPException(status_code=422,detail="Insira a unidade de medida do produto!")
            if(id_supplier is None or id_supplier==""):
                raise HTTPException(status_code=422,detail="Insira o fornecedor para o produto!")
            if(id_category is None or id_category ==""):
                raise HTTPException(status_code=422,detail="insira a categoria do produto!")
           
            ProductController.cursor.execute("UPDATE tblproduto SET produto = :1, valor = :2, status = :3, unidade_medida = :4, id_fornecedor = :5, id_categoria = :6 WHERE id = :7", [product, price, status, unit_measure, id_supplier, id_category, id_product])            
            ProductController.connection.commit()  
            print(ProductController.cursor.rowcount, "Rows Inserted")
        except DatabaseError as e:
            raise HTTPException(status_code=500, detail="Erro ao editar produto no banco de dados: " + str(e))
    
    ##FAZER A PARTE DE EXCLUISÃO E DE RETORNAR TODOS OS PRODUTOS
    ##PEGAR DE BASE A CATEGORIA