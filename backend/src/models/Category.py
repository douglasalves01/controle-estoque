from pydantic import BaseModel
from typing import Optional

class CategoryRequest(BaseModel):
    category: str
