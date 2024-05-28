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
            ReportsController.cursor.execute("SELECT e.ID,e.ESTOQUE_ATUAL, e.ESTOQUE_MINIMO, e.LOCALIZACAO, TO_CHAR(e.DATA_ULTIMA_ATUALIZACAO, 'YYYY-MM-DD HH24:MI:SS'),p.PRODUTO, e.CUSTO_UNITARIO FROM tblestoque e,tblproduto p where p.id=e.id_produto")
            rows = ReportsController.cursor.fetchall()
            return rows
        except DatabaseError as e:
            raise HTTPException(status_code=500, detail="Erro ao retornar estoques do banco de dados: " + str(e))
    
    @staticmethod
    def getAllMovements():
        try:
            ReportsController.cursor.execute("SELECT c.ID,c.tipo_transacao, TO_CHAR(c.data_hora_transacao, 'YYYY-MM-DD HH24:MI:SS'),c.quantidade,c.custo_unitario,c.motivo_transacao,p.PRODUTO,u.nome,p.ID  FROM tblcontroleestoque c,tblproduto p, tblusuario u where p.id=c.id_produto and u.id=c.id_usuario")
            rows = ReportsController.cursor.fetchall()
            return rows
        except DatabaseError as e:
            raise HTTPException(status_code=500, detail="Erro ao retornar movimentações do banco de dados: " + str(e))
    
    @staticmethod
    def getAllSales():
        try:
            ReportsController.cursor.execute("select vi.id,vi.quantidade,p.valor,(vi.quantidade * p.valor) AS total,TO_CHAR(v.data,'YYYY-MM-DD HH24:MI:SS'),vi.id_venda,u.nome from tblvenda v, tblusuario u,tblvendaitem vi, tblproduto p where v.id_usuario=u.id and vi.id_venda=v.id and p.id=vi.id_produto")
            rows = ReportsController.cursor.fetchall()
            return rows
        except DatabaseError as e:
            raise HTTPException(status_code=500, detail="Erro ao retornar movimentações do banco de dados: " + str(e))
    @staticmethod
    ##CONTA LUCRO   
    def getAllProfitSales():
        try:
            ReportsController.cursor.execute("select v.id,v.valor,TO_CHAR(v.data,'YYYY-MM-DD HH24:MI:SS'),sum(((vi.quantidade*p.valor)*c.comissao_venda/100) + ((vi.quantidade*p.valor)*c.custo_fixo/100)+ ((vi.quantidade*p.valor)*p.icms/100) )as custoTotal ,v.valor - sum(((vi.quantidade*p.valor)*c.comissao_venda/100) + ((vi.quantidade*p.valor)*c.custo_fixo/100)+ ((vi.quantidade*p.valor)*p.icms/100) ) from tblvendaitem vi,tblproduto p,tblconfig c,tblvenda v where vi.id_produto=p.id and vi.id_venda=v.id GROUP BY v.id,v.valor,v.data,c.margem_lucro,c.comissao_venda,c.custo_fixo")
            rows = ReportsController.cursor.fetchall()
            return rows
        except DatabaseError as e:
            raise HTTPException(status_code=500, detail="Erro ao retornar movimentações do banco de dados: " + str(e))
    @staticmethod
    def getQtdeSales():
        try:
            ReportsController.cursor.execute("select count(id) from tblvenda")
            rows = ReportsController.cursor.fetchall()
            return rows
        except DatabaseError as e:
            raise HTTPException(status_code=500, detail="Erro ao retornar quantidade de vendas do banco de dados: " + str(e))
    @staticmethod
    def getQtdeSuppliers():
        try:
            ReportsController.cursor.execute("select count(id) from tblfornecedor")
            rows = ReportsController.cursor.fetchall()
            return rows
        except DatabaseError as e:
            raise HTTPException(status_code=500, detail="Erro ao retornar quantidade de fornecedores do banco de dados: " + str(e))
    @staticmethod
    def getQtdeCategories():
        try:
            ReportsController.cursor.execute("select count(id) from tblcategoria")
            rows = ReportsController.cursor.fetchall()
            return rows
        except DatabaseError as e:
            raise HTTPException(status_code=500, detail="Erro ao retornar quantidade de categorias do banco de dados: " + str(e))
    @staticmethod
    def getQtdeProducts():
        try:
            ReportsController.cursor.execute("select count(id) from tblproduto")
            rows = ReportsController.cursor.fetchall()
            return rows
        except DatabaseError as e:
            raise HTTPException(status_code=500, detail="Erro ao retornar quantidade de produtos do banco de dados: " + str(e))
    @staticmethod
    def getProductStockMinimum():
        try:
            ReportsController.cursor.execute("select p.id,p.produto,p.DESCRICAO from tblproduto p,tblestoque e where e.id_produto=p.id and (e.ESTOQUE_ATUAL<=e.ESTOQUE_MINIMO)")
            rows = ReportsController.cursor.fetchall()
            return rows
        except DatabaseError as e:
            raise HTTPException(status_code=500, detail="Erro ao retornar quantidade de produtos com estoque minimos do banco de dados: " + str(e))

