from fastapi import APIRouter, Depends,HTTPException, Request
from controllers.ProductController import ProductController
from models.Product import ProductRequest
from fastapi.responses import JSONResponse
from helpers.check_token import checkToken
from roles.user import SimpleAuthBackend

routerProduct = APIRouter()

@routerProduct.post("/cadastrar/produto")
async def createProduct(product:ProductRequest,request:Request,token:str=Depends(SimpleAuthBackend().authenticate)):
    try:
        #chamar a function do controller para cadastrar um novo produto
        SimpleAuthBackend().verifyAccess(request,nivel_description="editor")
        ProductController.createProduct(product.product,product.price,product.status,product.unit_measure,product.id_supplier,product.id_category)
        return {"message":"Produto registrado com sucesso!"}

    except Exception as e:
        raise HTTPException(status_code=422,detail=str(e))
    
@routerProduct.put("/editar/produto/{id_product}")
async def updateProduct(id_product,product:ProductRequest,request:Request,token:str=Depends(SimpleAuthBackend().authenticate)):
    try:
        #chamar a function do controller para cadastrar um novo produto
        SimpleAuthBackend().verifyAccess(request,nivel_description="editor")
        ProductController.updateProduct(product.product,product.price,product.status,product.unit_measure,product.id_supplier,product.id_category, id_product)
        return {"message":"Produto editado com sucesso!"}

    except Exception as e:
        raise HTTPException(status_code=422,detail=str(e))