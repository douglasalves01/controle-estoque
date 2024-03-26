from database.conn import conn
from oracledb import DatabaseError
from fastapi import HTTPException

class SupplierController:
    connection = conn()
    cursor = connection.cursor()

    @staticmethod
    def createSupplier(cnpj, razao_social, nome, endereco, telefone):
        try:
            if not razao_social or not nome or not endereco or not telefone:
                raise HTTPException(status_code=422, detail="Preencha todos os campos obrigatórios!")
            
            SupplierController.cursor.execute("SELECT * FROM tblfornecedor WHERE cnpj = :1", [cnpj])
            rows = SupplierController.cursor.fetchall()
            if rows:
                raise HTTPException(status_code=422, detail="Este fornecedor já está cadastrado!")

            SupplierController.cursor.execute("INSERT INTO tblfornecedor (cnpj, razao_social, nome, endereco, telefone) VALUES (:1, :2, :3, :4, :5)", [cnpj, razao_social, nome, endereco, telefone]) 
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
    def updateSupplier(cnpj, razao_social, nome, endereco, telefone, supplier_id):
        try:
            if not razao_social or not nome or not endereco or not telefone:
                raise HTTPException(status_code=422, detail="Preencha todos os campos obrigatórios!")

            SupplierController.cursor.execute("UPDATE tblfornecedor SET cnpj = :1, razao_social = :2, nome = :3, endereco = :4, telefone = :5 WHERE id = :6", [cnpj, razao_social, nome, endereco, telefone, supplier_id])
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