from fastapi import APIRouter, Depends,HTTPException, Request
from controllers.SaleController import SaleController
from models.Sale import SaleRequest
from fastapi.responses import JSONResponse
from helpers.check_token import checkToken
from roles.user import SimpleAuthBackend

routerSale=APIRouter()
SaleController=SaleController()

@routerSale.post("/venda")
async def sale(sale:SaleRequest,request:Request, token:str=Depends(SimpleAuthBackend().authenticate)):
    try:
        SimpleAuthBackend().verifyAccess(request,nivel_description="admin")
        await SaleController.Sale(sale.id_produto,sale.quantidade,request)
        return {"message":"Venda registrada com sucesso!"}
    except Exception as e:
        raise HTTPException(status_code=422,detail=str(e))