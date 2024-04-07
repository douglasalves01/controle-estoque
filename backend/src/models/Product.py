from pydantic import BaseModel

class ProductRequest(BaseModel):
    product: str
    price: float
    status:str
    unit_measure:str
    id_supplier: str = ""
    id_category: str = ""