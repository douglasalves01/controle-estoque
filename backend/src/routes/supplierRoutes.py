from fastapi import APIRouter, HTTPException, Request
from controllers.SupplierController import SupplierController
from models.Supplier import SupplierRequest
from fastapi.responses import JSONResponse
from helpers.check_token import checkToken
from helpers.check_token_verify_access import check_token_and_verify_access

routerSupplier = APIRouter()
SupplierController = SupplierController()

@routerSupplier.post("/cadastrar/fornecedor")
@check_token_and_verify_access(nivel_description='editor')
async def create_supplier(supplier:SupplierRequest, request:Request):
    try:
        checkToken(request)
        SupplierController.createSupplier(supplier.supplier)
        return {"message": "Fornecedor cadastrado com sucesso!"}
    except HTTPException as e:
        raise HTTPException(status_code=422,detail=str(e))

@routerSupplier.get("/fornecedores")
@check_token_and_verify_access(nivel_description='editor')
async def get_all_suppliers(request: Request):
    try:
        checkToken(request)
        rows = SupplierController.getAllSuppliers()
        return JSONResponse(content=rows)
    except Exception as e:
        raise HTTPException(status_code=422,detail=str(e))
      
@routerSupplier.put("/editar/fornecedor/{supplier_id}")
@check_token_and_verify_access(nivel_description='editor')
async def updateSupplier(id_supplier,supplier:SupplierRequest,request:Request):
    try:
        checkToken(request)
        SupplierController.updateSupplier(supplier.supplier,id_supplier)
        return {"message":"Fornecedor editado com sucesso!"}
    except Exception as e:
        raise HTTPException(status_code=422,detail=str(e))

@routerSupplier.delete("/excluir/fornecedor/{supplier_id}")
@check_token_and_verify_access(nivel_description='editor')
async def deleteSupplier(id_supplier,request:Request):
    try:
        checkToken(request)
        SupplierController.deleteSupplier(id_supplier)
        return {"message":"Fornecedor excluído com sucesso!"}
    except Exception as e:
        raise HTTPException(status_code=422,detail=str(e))