from pydantic import BaseModel

class CategoryRequest(BaseModel):
    category: str
    status: str = "ativo"
