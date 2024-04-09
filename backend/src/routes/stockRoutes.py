from fastapi import APIRouter, Depends,HTTPException, Request
from controllers.StockController import StockController
from models.Stock import StockRequest
from fastapi.responses import JSONResponse
from helpers.check_token import checkToken
from roles.user import SimpleAuthBackend

routerStock=APIRouter()
StockController=StockController()

@routerStock.post("/controle-estoque/entrada/:id")
async def sale(stock:StockRequest,request:Request, token:str=Depends(SimpleAuthBackend().authenticate)):
    try:
        SimpleAuthBackend().verifyAccess(request,nivel_description="estoque")
        await StockController.Entrada(stock.addStock,stock.id_product,stock.description,stock.unitCost,request)
        return {"message":"Entrada no estoque registrada com sucesso!"}
    except Exception as e:
        raise HTTPException(status_code=422,detail=str(e))