from fastapi import APIRouter,HTTPException,Depends
from controllers.UserController import UserController
from models.User import UserRequest
from fastapi.responses import JSONResponse
from helpers.check_token import checkToken
from helpers.get_token import get_token
from fastapi import Request
routerUser=APIRouter()

@routerUser.get("/teste")
async def login(request:Request):
    token=checkToken(request)
    return JSONResponse(content=token)
    

@routerUser.post("/login")
async def Login(user:UserRequest):
    try:
        #chamar function do controller e passar os dados
        token = UserController.login(user.name,user.password)
        return JSONResponse(content=token)
    except Exception as e:
        raise HTTPException(status_code=422,detail=str(e))

@routerUser.post("/register")
async def Register(user:UserRequest):
    try:
        UserController.register(user.name,user.password)
        return {"message":"Usuário criado com sucesso!"}
    except Exception as e:
        raise HTTPException(status_code=422,detail=str(e))
