from fastapi import APIRouter,HTTPException, Request
from controllers.CategoryController import CategoryController
from models.Category import CategoryRequest
from fastapi.responses import JSONResponse
from helpers.check_token import checkToken
from helpers.check_token_verify_access import check_token_and_verify_access

routerCategory=APIRouter()
CategoryController=CategoryController()

@routerCategory.post("/cadastrar/categoria")
@check_token_and_verify_access(nivel_description='editor')
async def createCategory(category:CategoryRequest, request:Request):
    try:
        #chamar function do controller e passar a categoria
        checkToken(request)
        CategoryController.createCategory(category.category)
        return {"message":"Categoria registrada com sucesso!"}
    except Exception as e:
        raise HTTPException(status_code=422,detail=str(e))

@routerCategory.get("/categorias")
@check_token_and_verify_access(nivel_description='editor')
async def getAllCategory(request:Request):
    try:
        checkToken(request)
        rows = CategoryController.getAllCategory()
        return JSONResponse(content=rows)
    except Exception as e:
        raise HTTPException(status_code=422,detail=str(e))
    
@routerCategory.put("/editar/categoria/{id_category}")
@check_token_and_verify_access(nivel_description='editor')
async def updateCategory(id_category,category:CategoryRequest,request:Request):
    try:
        checkToken(request)
        CategoryController.updateCategory(category.category,id_category)
        return {"message":"Categoria editada com sucesso!"}
    except Exception as e:
        raise HTTPException(status_code=422,detail=str(e))

@routerCategory.delete("/excluir/categoria/{id_category}")
@check_token_and_verify_access(nivel_description='editor')
async def deleteCategory(id_category,request:Request):
    try:
        checkToken(request)
        CategoryController.deleteCategory(id_category)
        return {"message":"Categoria excluída com sucesso!"}
    except Exception as e:
        raise HTTPException(status_code=422,detail=str(e))