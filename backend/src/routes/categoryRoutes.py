from fastapi import APIRouter,HTTPException
from controllers.CategoryController import CategoryController
from models.Category import CategoryRequest
routerCategory=APIRouter()
CategoryController=CategoryController()

@routerCategory.post("/cadastrar/categoria")
async def createCategory(category:CategoryRequest):
    try:
        #chamar function do controller e passar a categoria
        CategoryController.createCategory(category.category)
        return {"message":"Categoria registrada com sucesso!"}
    except Exception as e:
        raise HTTPException(status_code=422,detail=str(e))