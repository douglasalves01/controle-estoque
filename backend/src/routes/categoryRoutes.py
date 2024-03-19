from fastapi import APIRouter,HTTPException
from controllers.CategoryController import CategoryController
from models.Category import CategoryRequest
from oracledb import DatabaseError
routerCategory=APIRouter()
CategoryController=CategoryController()

@routerCategory.post("/cadastrar/categoria")
async def createCategory(category:CategoryRequest):
    try:
        #chamar function do controller e passar a categoria
        CategoryController.createCategory(category.category)
        return {"message":"Categoria registrada com sucesso!"}
    except DatabaseError as e:
        raise HTTPException(status_code=500, detail="Erro ao inserir categoria no banco de dados: " + str(e))
    except Exception as e:
        raise HTTPException(status_code=422,detail=str(e))
    