from fastapi import APIRouter,HTTPException
from controllers.CategoryController import CategoryController
from models.Category import CategoryRequest
from fastapi.responses import JSONResponse

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

@routerCategory.get("/categorias")
async def getAllCategory():
    try:
        rows = CategoryController.getAllCategory()
        return JSONResponse(content=rows)
    except Exception as e:
        raise HTTPException(status_code=422,detail=str(e))
    
@routerCategory.put("/editar/categoria/{id_category}")
async def updateCategory(id_category,category:CategoryRequest):
    try:
        CategoryController.updateCategory(category.category,id_category)
        return {"message":"Categoria editada com sucesso!"}
    except Exception as e:
        raise HTTPException(status_code=422,detail=str(e))

@routerCategory.delete("/excluir/categoria/{id_category}")
async def deleteCategory(id_category):
    try:
        CategoryController.deleteCategory(id_category)
        return {"message":"Categoria excluída com sucesso!"}
    except Exception as e:
        raise HTTPException(status_code=422,detail=str(e))