from fastapi import APIRouter, Depends,HTTPException, Request
from controllers.CategoryController import CategoryController
from models.Category import CategoryRequest
from fastapi.responses import JSONResponse
from helpers.check_token import checkToken
from roles.user import SimpleAuthBackend

routerCategory=APIRouter()
CategoryController=CategoryController()

@routerCategory.post("/cadastrar/categoria")
async def createCategory(category:CategoryRequest, request:Request, token:str=Depends(SimpleAuthBackend().authenticate)):
    try:
        #chamar function do controller e passar a categoria
        SimpleAuthBackend().verifyAccess(request,nivel_description="editor")
        CategoryController.createCategory(category.category)
        return {"message":"Categoria registrada com sucesso!"}
    except Exception as e:
        raise HTTPException(status_code=422,detail=str(e))

@routerCategory.get("/categorias")
async def getAllCategory(request:Request,token:str=Depends(SimpleAuthBackend().authenticate)):
    try:
        SimpleAuthBackend().verifyAccess(request,nivel_description="editor")
        rows = CategoryController.getAllCategory()
        return JSONResponse(content=rows)
    except Exception as e:
        raise HTTPException(status_code=422,detail=str(e))
    
@routerCategory.put("/editar/categoria/{id_category}")
async def updateCategory(id_category,category:CategoryRequest,request:Request,token:str=Depends(SimpleAuthBackend().authenticate)):
    try:
        SimpleAuthBackend().verifyAccess(request,nivel_description="editor")
        CategoryController.updateCategory(category.category,id_category)
        return {"message":"Categoria editada com sucesso!"}
    except Exception as e:
        raise HTTPException(status_code=422,detail=str(e))

@routerCategory.delete("/excluir/categoria/{id_category}")
async def deleteCategory(id_category,request:Request,token:str=Depends(SimpleAuthBackend().authenticate)):
    try:
        SimpleAuthBackend().verifyAccess(request,nivel_description="editor")
        CategoryController.deleteCategory(id_category)
        return {"message":"Categoria excluída com sucesso!"}
    except Exception as e:
        raise HTTPException(status_code=422,detail=str(e))