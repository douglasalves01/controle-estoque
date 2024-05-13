from fastapi import APIRouter, Depends,HTTPException, Request
from controllers.ConfigController import ConfigController
from models.Config import ConfigRequest
from fastapi.responses import JSONResponse
from roles.user import SimpleAuthBackend

routerConfig=APIRouter()
ConfigController=ConfigController()

@routerConfig.get("/configs")
async def getAllConfig(request:Request):
    try:
        rows = ConfigController.getAllConfig()
        return JSONResponse(content=rows)
    except Exception as e:
        raise HTTPException(status_code=422,detail=str(e))
       
@routerConfig.put("/config/{id}")
async def updateConfig(id,config:ConfigRequest,request:Request,token:str=Depends(SimpleAuthBackend().authenticate)):
    try:
        SimpleAuthBackend().verifyAccess(request,nivel_description="admin")
        ConfigController.configSave(config.margem_lucro,config.comissao_venda,config.custo_fixo,config.imposto_venda,id)
        return {"message":"Configurações salvas com sucesso!"}
    except Exception as e:
        raise HTTPException(status_code=422,detail=str(e))

