from database.conn import conn
from oracledb import DatabaseError
from fastapi import HTTPException

class CategoryController:
    connection = conn()
    cursor = connection.cursor()
    #metodo para salvar uma categoria
    @staticmethod
    def createCategory(category, status):
        #criação de categoria
        try:
            #verificar se a categoria veio nula ou vazia
            if(category is None or category==""):
                raise HTTPException(status_code=422, detail="Insira o nome da categoria!")
            categoryFormat=category.lower()
            #verificar se já existe uma categoria com o mesmo nome salva no banco
            CategoryController.cursor.execute("select * from tblcategoria where categoria = (:1)",[categoryFormat])
            rows = CategoryController.cursor.fetchall()
            if(rows):
                raise HTTPException(status_code=422, detail="Categoria já existe no banco de dados!")
            #insert na tabela categoria
            CategoryController.cursor.execute("INSERT INTO TBLCATEGORIA (CATEGORIA, STATUS) VALUES (:1, :2)", [categoryFormat, status])
            CategoryController.connection.commit()  
            print(CategoryController.cursor.rowcount, "Rows Inserted")
        except DatabaseError as e:
            raise HTTPException(status_code=500, detail="Erro ao inserir categoria no banco de dados: " + str(e))
    
    #método para retornar todas as categorias    
    @staticmethod
    def getAllCategory():
        try:
            CategoryController.cursor.execute("select * from tblcategoria")
            rows = CategoryController.cursor.fetchall()
            return rows
        except DatabaseError as e:
            raise HTTPException(status_code=500, detail="Erro ao retornar categorias do banco de dados: " + str(e))
    #método para retornar todas as categorias ativas  
    @staticmethod
    def getAllCategoryActive():
        try:
            CategoryController.cursor.execute("select * from tblcategoria where status='ativo'")
            rows = CategoryController.cursor.fetchall()
            return rows
        except DatabaseError as e:
            raise HTTPException(status_code=500, detail="Erro ao retornar categorias do banco de dados: " + str(e))
    
    #metodo para editar uma categoria
    @staticmethod
    def updateCategory(category, id, status):
        try:
            if(category is None or category==""):
                raise HTTPException(status_code=422, detail="Insira o nome da categoria!")
            if(status is None or status==""):
                raise HTTPException(status_code=422, detail="Insira o status da categoria!")
            CategoryController.cursor.execute("UPDATE tblcategoria SET categoria = :1, status = :2 WHERE id = :3", [category,status,id])
            CategoryController.connection.commit()
        except DatabaseError as e:
            raise HTTPException(status_code=500, detail="Erro ao retornar categorias do banco de dados: " + str(e))
    
    #metodo para deletar uma categoria
    @staticmethod
    def deleteCategory(id):
        try:
            print(id)
            status="inativo"
            CategoryController.cursor.execute("UPDATE tblcategoria SET status = :1 WHERE id = :2", [status,id])
            CategoryController.connection.commit()
        except DatabaseError as e:
            raise HTTPException(status_code=500, detail="Erro ao excluir categoria do banco de dados: " + str(e))