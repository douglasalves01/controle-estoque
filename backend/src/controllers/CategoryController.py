from database.conn import conn
from oracledb import DatabaseError
class CategoryController:
    connection = conn()
    cursor = connection.cursor()
    @staticmethod
    def createCategory(category):
        #criação de categoria
        try:
             with CategoryController.cursor as cursor:
                cursor.executemany("INSERT INTO tblcategoria (cateogria) VALUES (:1)", category)
                print(cursor.rowcount, "Rows Inserted")
        except DatabaseError as e:
            print("Erro ao criar tabela estoque:", e)
       
        print(f'aqui e a categoria de {category}')
        pass