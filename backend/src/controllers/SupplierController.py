from database.conn import conn
from oracledb import DatabaseError
from fastapi import HTTPException

class SupplierController:
    connection = conn()
    cursor = connection.cursor()

    @staticmethod
    def createSupplier(supplier_name):
        try:
            if not supplier_name:
                raise HTTPException(status_code=422, detail="Insira o nome do fornecedor!")
            
            supplier_name_format = supplier_name.lower()
            
            SupplierController.cursor.execute("SELECT * FROM tblfornecedor WHERE nome = :1", [supplier_name_format])
            rows = SupplierController.cursor.fetchall()
            if rows:
                raise HTTPException(status_code=422, detail="Este fornecedor já está cadastrado!")

            SupplierController.cursor.execute("INSERT INTO tblfornecedor (nome) VALUES (:1)", [supplier_name_format]) 
            SupplierController.connection.commit()  
            print(SupplierController.cursor.rowcount, "Linhas inseridas")
        except DatabaseError as e:
            raise HTTPException(status_code=500, detail="Erro ao inserir fornecedor no banco de dados: " + str(e))
    
    @staticmethod
    def getAllSuppliers():
        try:
            SupplierController.cursor.execute("SELECT * FROM tblfornecedor")
            rows = SupplierController.cursor.fetchall()
            return rows
        except DatabaseError as e:
            raise HTTPException(status_code=500, detail="Erro ao retornar fornecedores do banco de dados: " + str(e))
    
    @staticmethod
    def updateSupplier(supplier_name, supplier_id):
        try:
            if not supplier_name:
                raise HTTPException(status_code=422, detail="Insira o nome do fornecedor!")
            
            SupplierController.cursor.execute("UPDATE tblfornecedor SET nome = :1 WHERE id = :2", [supplier_name, supplier_id])
            SupplierController.connection.commit()
        except DatabaseError as e:
            raise HTTPException(status_code=500, detail="Erro ao atualizar fornecedor no banco de dados: " + str(e))
    
    @staticmethod
    def deleteSupplier(supplier_id):
        try:
            SupplierController.cursor.execute("DELETE FROM tblfornecedor WHERE id = :1", [supplier_id])
            SupplierController.connection.commit()
        except DatabaseError as e:
            raise HTTPException(status_code=500, detail="Erro ao excluir fornecedor do banco de dados: " + str(e))