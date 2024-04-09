from pydantic import BaseModel

class StockRequest(BaseModel):
    addStock: int = 0
    unitCost: float =0
    description:str=""
    id_product: int = ""