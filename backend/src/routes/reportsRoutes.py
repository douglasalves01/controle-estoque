#relatorio de produtos
#relatorio de categorias
#relatorio de fornecedores
#relatorio de movimentações
#relatorio do estoque

from fastapi import APIRouter, Depends,HTTPException, Request
from controllers.ReportsController import ReportsController
from models.Category import CategoryRequest
from fastapi.responses import JSONResponse
from helpers.check_token import checkToken
from roles.user import SimpleAuthBackend

routerReports=APIRouter()

@routerReports.get("/relatorio/categorias")
async def reportProduct(request:Request,token:str=Depends(SimpleAuthBackend().authenticate)):
    try:
        SimpleAuthBackend().verifyAccess(request,nivel_description="supervisor")
        rows = ReportsController.getAllCategories()
        return JSONResponse(content=rows)
    except Exception as e:
        raise HTTPException(status_code=422,detail=str(e))
    
@routerReports.get("/relatorio/produtos")
async def reportProduct(request:Request,token:str=Depends(SimpleAuthBackend().authenticate)):
    try:
        SimpleAuthBackend().verifyAccess(request,nivel_description="supervisor")
        rows = ReportsController.getAllProducts()
        return JSONResponse(content=rows)
    except Exception as e:
        raise HTTPException(status_code=422,detail=str(e))
    
@routerReports.get("/relatorio/fornecedores")
async def reportProduct(request:Request,token:str=Depends(SimpleAuthBackend().authenticate)):
    try:
        SimpleAuthBackend().verifyAccess(request,nivel_description="supervisor")
        rows = ReportsController.getAllSuppliers()
        return JSONResponse(content=rows)
    except Exception as e:
        raise HTTPException(status_code=422,detail=str(e))
    
@routerReports.get("/relatorio/estoques")
async def reportProduct(request:Request,token:str=Depends(SimpleAuthBackend().authenticate)):
    try:
        SimpleAuthBackend().verifyAccess(request,nivel_description="supervisor")
        rows = ReportsController.getAllStocks()
        return JSONResponse(content=rows)
    except Exception as e:
        raise HTTPException(status_code=422,detail=str(e))
@routerReports.get("/relatorio/movimentacoes")
async def reportProduct(request:Request,token:str=Depends(SimpleAuthBackend().authenticate)):
    try:
        SimpleAuthBackend().verifyAccess(request,nivel_description="supervisor")
        rows = ReportsController.getAllMovements()
        return JSONResponse(content=rows)   
    except Exception as e:
        raise HTTPException(status_code=422,detail=str(e))
    
@routerReports.get("/relatorio/sales")
async def reportProduct(request:Request,token:str=Depends(SimpleAuthBackend().authenticate)):
    try:
        SimpleAuthBackend().verifyAccess(request,nivel_description="supervisor")
        rows = ReportsController.getAllSales()
        return JSONResponse(content=rows)
    except Exception as e:
        raise HTTPException(status_code=422,detail=str(e))
@routerReports.get("/financeiro/sales")
async def reportProduct(request:Request,token:str=Depends(SimpleAuthBackend().authenticate)):
    try:
        SimpleAuthBackend().verifyAccess(request,nivel_description="supervisor")
        rows = ReportsController.getAllProfitSales()
        return JSONResponse(content=rows)
    except Exception as e:
        raise HTTPException(status_code=422,detail=str(e))
@routerReports.get("/quantidade/sales")
async def reportProduct(request:Request,token:str=Depends(SimpleAuthBackend().authenticate)):
    try:
        SimpleAuthBackend().verifyAccess(request,nivel_description="supervisor")
        rows = ReportsController.getQtdeSales()
        return JSONResponse(content=rows)
    except Exception as e:
        raise HTTPException(status_code=422,detail=str(e))
@routerReports.get("/quantidade/categories")
async def reportProduct(request:Request,token:str=Depends(SimpleAuthBackend().authenticate)):
    try:
        SimpleAuthBackend().verifyAccess(request,nivel_description="supervisor")
        rows = ReportsController.getQtdeCategories()
        return JSONResponse(content=rows)
    except Exception as e:
        raise HTTPException(status_code=422,detail=str(e))
@routerReports.get("/quantidade/suppliers")
async def reportProduct(request:Request,token:str=Depends(SimpleAuthBackend().authenticate)):
    try:
        SimpleAuthBackend().verifyAccess(request,nivel_description="supervisor")
        rows = ReportsController.getQtdeSuppliers()
        return JSONResponse(content=rows)
    except Exception as e:
        raise HTTPException(status_code=422,detail=str(e))
@routerReports.get("/quantidade/products")
async def reportProduct(request:Request,token:str=Depends(SimpleAuthBackend().authenticate)):
    try:
        SimpleAuthBackend().verifyAccess(request,nivel_description="supervisor")
        rows = ReportsController.getQtdeProducts()
        return JSONResponse(content=rows)
    except Exception as e:
        raise HTTPException(status_code=422,detail=str(e))
@routerReports.get("/notificacao/products")
async def reportProduct(request:Request,token:str=Depends(SimpleAuthBackend().authenticate)):
    try:
        SimpleAuthBackend().verifyAccess(request,nivel_description="supervisor")
        rows = ReportsController.getProductStockMinimum()
        return JSONResponse(content=rows)
    except Exception as e:
        raise HTTPException(status_code=422,detail=str(e))
