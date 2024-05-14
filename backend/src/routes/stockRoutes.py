from fastapi import APIRouter, Depends,HTTPException, Request
from controllers.StockController import StockController
from models.Stock import StockRequest
from roles.user import SimpleAuthBackend

routerStock=APIRouter()
StockController=StockController()

@routerStock.post("/controle-estoque/movimentacao/{id_product}")
async def sale(id_product,stock:StockRequest,request:Request, token:str=Depends(SimpleAuthBackend().authenticate)):
    try:
        SimpleAuthBackend().verifyAccess(request,nivel_description="estoque")
        await StockController.Movimentacao(stock.addStock,id_product,stock.description,stock.unitCost,stock.typeMoviment,request)
        return {"message":"Entrada no estoque registrada com sucesso!"}
    except Exception as e:
        raise HTTPException(status_code=422,detail=str(e))