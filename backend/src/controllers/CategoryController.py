from database.conn import conn
from oracledb import DatabaseError
class CategoryController:
    connection = conn()
    cursor = connection.cursor()
    @staticmethod
    def createCategory(category):
        #criação de categoria
        try:
                CategoryController.cursor.execute("INSERT INTO TBLCATEGORIA (CATEGORIA) VALUES (:1)", [category]) 
                CategoryController.connection.commit()  
                print(CategoryController.cursor.rowcount, "Rows Inserted")
        except DatabaseError as e:
            print("Erro na inserção:", e)
        pass
        

  