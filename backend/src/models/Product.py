from pydantic import BaseModel

class ProductRequest(BaseModel):
    product: str
    price: float
    status: str = "ativo"
    unit_measure:str
    id_supplier: str = ""
    id_category: str = ""
    currentStock: str = 0
    unitCost: str =0
    minimumStock: str = 0
    location: str = ""
    id_product: str = ""