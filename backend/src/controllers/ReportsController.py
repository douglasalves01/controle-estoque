from database.conn import conn
from oracledb import DatabaseError
from fastapi import HTTPException

class ReportsController:
    connection=conn()
    cursor=connection.cursor()

    @staticmethod
    def getAllCategories():
        try:
            ReportsController.cursor.execute("select * from tblcategoria")
            rows = ReportsController.cursor.fetchall()
            return rows
        except DatabaseError as e:
            raise HTTPException(status_code=500, detail="Erro ao retornar categorias do banco de dados: " + str(e))
    
    @staticmethod
    def getAllProducts():
        try:
            ReportsController.cursor.execute("select * from tblproduto")
            rows = ReportsController.cursor.fetchall()
            return rows
        except DatabaseError as e:
            raise HTTPException(status_code=500, detail="Erro ao retornar produtos do banco de dados: " + str(e))
    
    @staticmethod
    def getAllSuppliers():
        try:
            ReportsController.cursor.execute("select f.id,f.cnpj,f.razao_social,f.nome_fantasia,f.endereco, t.telefone from tblfornecedor f, tbltelefone t where f.id=t.id")
            rows = ReportsController.cursor.fetchall()
            return rows
        except DatabaseError as e:
            raise HTTPException(status_code=500, detail="Erro ao retornar fornecedores do banco de dados: " + str(e))
    
    @staticmethod
    def getAllStocks():
        try:
            ReportsController.cursor.execute("SELECT p.PRODUTO,e.ESTOQUE_ATUAL, e.ESTOQUE_MINIMO, e.LOCALIZACAO, e.CUSTO_UNITARIO, TO_CHAR(e.DATA_ULTIMA_ATUALIZACAO, 'YYYY-MM-DD HH24:MI:SS') FROM tblestoque e,tblproduto p where p.id=e.id_produto")
            rows = ReportsController.cursor.fetchall()
            return rows
        except DatabaseError as e:
            raise HTTPException(status_code=500, detail="Erro ao retornar estoques do banco de dados: " + str(e))
    
    @staticmethod
    def getAllMovements():
        try:
            ReportsController.cursor.execute("SELECT p.PRODUTO,c.tipo_transacao, TO_CHAR(c.data_hora_transacao, 'YYYY-MM-DD HH24:MI:SS'), c.motivo_transacao, c.quantidade,c.custo_unitario, u.nome FROM tblcontroleestoque c,tblproduto p, tblusuario u where p.id=c.id_produto and u.id=c.id_usuario")
            rows = ReportsController.cursor.fetchall()
            return rows
        except DatabaseError as e:
            raise HTTPException(status_code=500, detail="Erro ao retornar movimentações do banco de dados: " + str(e))
    