from database.conn import conn
from oracledb import DatabaseError
from fastapi import HTTPException

class SupplierController:
    connection = conn()
    cursor = connection.cursor()

    @staticmethod
    def createSupplier(supplier_name, supplier_cnpj, supplier_razao_social, supplier_nome_fantasia, supplier_endereco, supplier_telefone):
        try:
            if not all([supplier_name, supplier_cnpj, supplier_razao_social, supplier_nome_fantasia, supplier_endereco, supplier_telefone]):
                raise HTTPException(status_code=422, detail="Todos os campos do fornecedor devem ser preenchidos!")

            supplier_name_format = supplier_name.lower()

            SupplierController.cursor.execute("SELECT * FROM tblfornecedor WHERE nome = :1", [supplier_name_format])
            rows_name = SupplierController.cursor.fetchall()
            if rows_name:
                raise HTTPException(status_code=422, detail="Este nome de fornecedor já está cadastrado!")

            SupplierController.cursor.execute("SELECT * FROM tblfornecedor WHERE cnpj = :1", [supplier_cnpj])
            rows_cnpj = SupplierController.cursor.fetchall()
            if rows_cnpj:
                raise HTTPException(status_code=422, detail="Este CNPJ já está cadastrado!")

            SupplierController.cursor.execute("SELECT * FROM tblfornecedor WHERE razao_social = :1", [supplier_razao_social])
            rows_razao_social = SupplierController.cursor.fetchall()
            if rows_razao_social:
                raise HTTPException(status_code=422, detail="Esta razão social já está cadastrada!")

            SupplierController.cursor.execute("SELECT * FROM tblfornecedor WHERE nome_fantasia = :1", [supplier_nome_fantasia])
            rows_nome_fantasia = SupplierController.cursor.fetchall()
            if rows_nome_fantasia:
                raise HTTPException(status_code=422, detail="Este nome fantasia já está cadastrado!")

            SupplierController.cursor.execute("SELECT * FROM tblfornecedor WHERE telefone = :1", [supplier_telefone])
            rows_telefone = SupplierController.cursor.fetchall()
            if rows_telefone:
                raise HTTPException(status_code=422, detail="Este telefone já está cadastrado!")

            SupplierController.cursor.execute("INSERT INTO tblfornecedor (nome, cnpj, razao_social, nome_fantasia, endereco, telefone) VALUES (:1, :2, :3, :4, :5, :6)", 
                                              [supplier_name_format, supplier_cnpj, supplier_razao_social, supplier_nome_fantasia, supplier_endereco, supplier_telefone]) 
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
    def updateSupplier(supplier_id, supplier_name, supplier_cnpj, supplier_razao_social, supplier_nome_fantasia, supplier_endereco, supplier_telefone):
        try:
            if not supplier_name or not supplier_cnpj or not supplier_razao_social or not supplier_nome_fantasia or not supplier_endereco or not supplier_telefone:
                raise HTTPException(status_code=422, detail="Todos os campos do fornecedor devem ser preenchidos!")
                
            SupplierController.cursor.execute("UPDATE tblfornecedor SET nome = :1, cnpj = :2, razao_social = :3, nome_fantasia = :4, endereco = :5, telefone = :6 WHERE id = :7", 
                                              [supplier_name, supplier_cnpj, supplier_razao_social, supplier_nome_fantasia, supplier_endereco, supplier_telefone, supplier_id])
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