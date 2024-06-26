from fastapi import APIRouter, HTTPException, Request, Depends
from controllers.SupplierController import SupplierController
from models.Supplier import SupplierRequest
from fastapi.responses import JSONResponse
from helpers.check_token import checkToken
from roles.user import SimpleAuthBackend

routerSupplier = APIRouter()
SupplierController = SupplierController()

@routerSupplier.post("/cadastrar/fornecedor")
async def createSupplier(supplier: SupplierRequest, request: Request, token: str = Depends(SimpleAuthBackend().authenticate)):
    try:
        SimpleAuthBackend().verifyAccess(request, nivel_description='editor')
        SupplierController.createSupplier(supplier.cnpj, supplier.razao_social, supplier.nome_fantasia, supplier.endereco, supplier.telefone,supplier.status)
        return {"message": "Fornecedor cadastrado com sucesso!"}
    except HTTPException as e:
        raise HTTPException(status_code=422, detail=str(e))

@routerSupplier.get("/fornecedores")
async def getAllSuppliers(request: Request, token: str = Depends(SimpleAuthBackend().authenticate)):
    try:
        SimpleAuthBackend().verifyAccess(request, nivel_description='editor')
        rows = SupplierController.getAllSuppliers()
        return JSONResponse(content=rows)
    except HTTPException as e:
        raise HTTPException(status_code=422, detail=str(e))
      
@routerSupplier.get("/fornecedores-active")
async def getAllSuppliers(request: Request, token: str = Depends(SimpleAuthBackend().authenticate)):
    try:
        SimpleAuthBackend().verifyAccess(request, nivel_description='editor')
        rows = SupplierController.getAllSuppliersActive()
        return JSONResponse(content=rows)
    except HTTPException as e:
        raise HTTPException(status_code=422, detail=str(e))
      
@routerSupplier.put("/editar/fornecedor/{supplier_id}")
async def updateSupplier(supplier_id: int, supplier: SupplierRequest, request: Request, token: str = Depends(SimpleAuthBackend().authenticate)):
    try:
        SimpleAuthBackend().verifyAccess(request, nivel_description='admin')
        SupplierController.updateSupplier(supplier_id,supplier.cnpj,supplier.razao_social,supplier.nome_fantasia,supplier.endereco,supplier.telefone,supplier.status)
        return {"message":"Fornecedor editado com sucesso!"}
    except HTTPException as e:
        raise HTTPException(status_code=422, detail=str(e))

@routerSupplier.delete("/excluir/fornecedor/{supplier_id}")
async def deleteSupplier(supplier_id: int, request: Request, token: str = Depends(SimpleAuthBackend().authenticate)):
    try:
        SimpleAuthBackend().verifyAccess(request, nivel_description='admin')
        SupplierController.deleteSupplier(supplier_id)
        return {"message":"Fornecedor excluído com sucesso!"}
    except HTTPException as e:
        raise HTTPException(status_code=422, detail=str(e))