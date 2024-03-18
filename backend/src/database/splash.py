from conn import conn
from oracledb import DatabaseError

connection = conn()

cursor = connection.cursor()
with cursor as cursor:
    try:
        cursor.execute("""
            create table tblestoque (
                id number generated always as identity,
                estoque_atual number(5),
                estoque_minimo number(5),
                localizacao varchar2(100),
                data_entrada date,
                data_ultima_atualizacao date,                   
                primary key (id))""")
        print("Tabela estoque criada")
    except DatabaseError as e:
        print("Erro ao criar tabela estoque:", e)

    try:
        cursor.execute("""
            create table tbltelefone (
                id number generated always as identity,
                telefone varchar2(12),                   
                primary key (id))""")
        print("Tabela telefone criada")
    except DatabaseError as e:
        print("Erro ao criar tabela telefone:", e)

    try:
        cursor.execute("""
            create table tblfornecedor (
                id number generated always as identity,
                CNPJ varchar2(14),                   
                razao_social varchar2(100),                   
                nome_fantasia varchar2(100),                   
                endereco varchar2(100),
                id_telefone number,                    
                primary key (id),
                foreign key (id_telefone) references tbltelefone(id))""")
        print("Tabela fornecedor criada")
    except DatabaseError as e:
        print("Erro ao criar tabela fornecedor:", e)

    try:
        cursor.execute("""
            create table tblusuario (
                id number generated always as identity,
                nome varchar2(30),                   
                senha varchar2(20),                                       
                primary key (id))""")
        print("Tabela usuario criada")
    except DatabaseError as e:
        print("Erro ao criar tabela usuario:", e)

    try:
        cursor.execute("""
            create table tblcategoria (
                id number generated always as identity,
                categoria varchar2(20),                                   
                primary key (id))""")
        print("Tabela categoria criada")
    except DatabaseError as e:
        print("Erro ao criar tabela categoria:", e)

    try:
        cursor.execute("""
            create table tblproduto (
                id number generated always as identity,
                produto varchar2(20),                   
                valor decimal(10,2),                   
                status varchar2(8),                   
                custo_unitario decimal(10,2),
                custo_medio decimal(10,2),
                unidade_medida varchar2(5),
                id_fornecedor number,                    
                id_categoria number,                    
                primary key (id),
                foreign key (id_fornecedor) references tblfornecedor(id),
                foreign key (id_categoria) references tblcategoria(id))""")
        print("Tabela produto criada")
    except DatabaseError as e:
        print("Erro ao criar tabela produto:", e)

    try:
        cursor.execute("""
            create table tblcontroleestoque (
                id number generated always as identity,
                tipo_transacao varchar2(20),                   
                data_hora_transacao date,                   
                motivo_transacao varchar2(100), 
                id_usuario number,                    
                id_produto number,                    
                primary key (id),
                foreign key (id_usuario) references tblusuario(id),
                foreign key (id_produto) references tblproduto(id))""")
        print("Tabela controle estoque criada")
    except DatabaseError as e:
        print("Erro ao criar tabela controle estoque:", e)

# Fechar a conexão
connection.close()
