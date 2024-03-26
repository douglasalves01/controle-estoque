from fastapi import APIRouter, HTTPException, Request
from controllers.SupplierController import SupplierController
from models.Supplier import SupplierRequest
from fastapi.responses import JSONResponse
from helpers.check_token import checkToken

routerSupplier = APIRouter()
SupplierController = SupplierController()

@routerSupplier.post("/cadastrar/fornecedor")
async def createSupplier(supplier: SupplierRequest, request: Request):
    try:
        checkToken(request)
        SupplierController.createSupplier(supplier.supplier)
        return {"message": "Fornecedor cadastrado com sucesso!"}
    except HTTPException as e:
        raise HTTPException(status_code=422, detail=str(e))

@routerSupplier.get("/fornecedores")
async def getAllSuppliers(request: Request):
    try:
        checkToken(request)
        rows = SupplierController.getAllSuppliers()
        return JSONResponse(content=rows)
    except Exception as e:
        raise HTTPException(status_code=422, detail=str(e))
      
@routerSupplier.put("/editar/fornecedor/{supplier_id}")
async def updateSupplier(supplier_id, supplier: SupplierRequest, request: Request):
    try:
        checkToken(request)
        SupplierController.updateSupplier(supplier.supplier, supplier_id)
        return {"message":"Fornecedor editado com sucesso!"}
    except Exception as e:
        raise HTTPException(status_code=422, detail=str(e))

@routerSupplier.delete("/excluir/fornecedor/{supplier_id}")
async def deleteSupplier(supplier_id, request: Request):
    try:
        checkToken(request)
        SupplierController.deleteSupplier(supplier_id)
        return {"message":"Fornecedor excluído com sucesso!"}
    except Exception as e:
        raise HTTPException(status_code=422, detail=str(e))