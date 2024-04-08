from pydantic import BaseModel

class StockRequest(BaseModel):
    currentStock: str = 0
    unitCost: str =0
    minimumStock: str = 0
    location: float
    id_product: str = ""