from fastapi import APIRouter,HTTPException,Depends
from controllers.UserController import UserController
from models.User import UserRequest
from fastapi.responses import JSONResponse
from fastapi import Request
from roles.user import SimpleAuthBackend

routerUser=APIRouter()

@routerUser.get("/items/")
async def read_items(request:Request,token: dict = Depends(SimpleAuthBackend().authenticate)):
    SimpleAuthBackend().verifyAccess(request,nivel_description='editor')
    return {"token": token,"message": "Items retrieved successfully"}

@routerUser.post("/login")
async def Login(user:UserRequest):
    try:
        #chamar function do controller e passar os dados
        token = UserController.login(user.name,user.password)
        return JSONResponse(content=token)
    except Exception as e:
        raise HTTPException(status_code=422,detail=str(e))

@routerUser.post("/register")
async def Register(user:UserRequest,request:Request,token: str = Depends(SimpleAuthBackend().authenticate)):
    try:
        SimpleAuthBackend().verifyAccess(request,nivel_description='admin')
        UserController.register(user.name,user.password,user.id_nivelacesso)
        return {"message":"Usuário criado com sucesso!"}
    except Exception as e:
        raise HTTPException(status_code=422,detail=str(e))
