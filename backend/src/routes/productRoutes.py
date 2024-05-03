from fastapi import APIRouter, Depends,HTTPException, Request
from controllers.ProductController import ProductController
from models.Product import ProductRequest
from models.Stock import StockRequest
from fastapi.responses import JSONResponse
from helpers.check_token import checkToken
from roles.user import SimpleAuthBackend

routerProduct = APIRouter()
ProductController = ProductController()

@routerProduct.post("/cadastrar/produto")
async def createProduct(product:ProductRequest,request:Request,token:str=Depends(SimpleAuthBackend().authenticate)):
    try:
        #chamar a function do controller para cadastrar um novo produto
        SimpleAuthBackend().verifyAccess(request,nivel_description="editor")
        ProductController.createProduct(product.product,product.price,product.status,product.unit_measure,product.id_supplier,product.id_category,product.currentStock,product.minimumStock,product.unitCost,product.location, request)
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

@routerProduct.get("/produto")
async def getAllProducts(request:Request,token:str=Depends(SimpleAuthBackend().authenticate)):
    try:
        SimpleAuthBackend().verifyAccess(request,nivel_description="editor")
        rows = ProductController.getAllProducts()
        return JSONResponse(content=rows)
    except Exception as e:
        raise HTTPException(status_code=422,detail=str(e))
    
    
@routerProduct.delete("/excluir/produto/{id_product}")
async def deleteProduct(id_product,request:Request,token:str=Depends(SimpleAuthBackend().authenticate)):
    try:
        SimpleAuthBackend().verifyAccess(request,nivel_description="editor")
        ProductController.deleteProduct(id_product)
        return {"message":"Produto excluído com sucesso!"}
    except Exception as e:
        raise HTTPException(status_code=422,detail=str(e))