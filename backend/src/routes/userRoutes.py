from fastapi import APIRouter,HTTPException,Depends
from controllers.UserController import UserController
from models.User import UserRequest
from fastapi.responses import JSONResponse
from helpers.check_token import checkToken
from fastapi import Request
from roles.user import verifyAccess
from helpers.check_token_verify_access import check_token_and_verify_access
routerUser=APIRouter()

@routerUser.get("/teste")
@check_token_and_verify_access(nivel_description='admin')
async def login(request:Request):
    return 'teste'
    
@routerUser.post("/login")
async def Login(user:UserRequest):
    try:
        #chamar function do controller e passar os dados
        token = UserController.login(user.name,user.password)
        return JSONResponse(content=token)
    except Exception as e:
        raise HTTPException(status_code=422,detail=str(e))

@routerUser.post("/register")
@check_token_and_verify_access(nivel_description='admin')#somente um admin pode cadastrar um usuário
async def Register(user:UserRequest):
    try:
        print(user.name)
        UserController.register(user.name,user.password,user.id_nivelacesso)
        return {"message":"Usuário criado com sucesso!"}
    except Exception as e:
        raise HTTPException(status_code=422,detail=str(e))
