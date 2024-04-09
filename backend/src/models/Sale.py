from typing import List
from pydantic import BaseModel

class SaleRequest(BaseModel):
    id_produto:List[str]
    quantidade:List[str]

