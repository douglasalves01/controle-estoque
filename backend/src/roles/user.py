from fastapi import Request
from helpers.get_user_by_token import getUserByToken
from database.conn import conn
from fastapi import HTTPException
from oracledb import DatabaseError
#admin = tudo liberado
#editor = cadastro/editar/excluir liberado 
#estoque = movimentações/relatórios/estoque
#supervisor = tudo liberado, menos a parte de criar usuário


def verifyAccess(request:Request, nivel_description):
    #vou receber o nivel do usuario e a descração do nivel
    try:
        connection = conn()
        cursor = connection.cursor()
        user=getUserByToken(request)
        cursor.execute("select n.nome from tblnivelacesso n,tblusuario u where u.nome = :1 and n.id = u.id_nivelacesso",[user] )
        result = cursor.fetchone()[0]
        if(nivel_description=='admin'):
            if not result =='admin':
                raise HTTPException(status_code=401, detail="Você não tem acesso para realizar essa operação! Contacte o administrador dos sistema!")
            return True
        elif(nivel_description=='editor'):
            if(result=='estoque'):
                raise HTTPException(status_code=401, detail="Você não tem acesso para realizar essa operação! Contacte o administrador dos sistema!")
            return True
        elif(nivel_description=="estoque"):
            if(result=='editor'):
                raise HTTPException(status_code=401, detail="Você não tem acesso para realizar essa operação! Contacte o administrador dos sistema!")
            return True
        elif(nivel_description=='supervisor'):
            if(result=='editor' or result=='estoque'):
                raise HTTPException(status_code=401, detail="Você não tem acesso para realizar essa operação! Contacte o administrador dos sistema!")
            return True
        return True
    except DatabaseError as e:
            raise HTTPException(status_code=500, detail="Erro ao fazer login: " + str(e))

      
    
