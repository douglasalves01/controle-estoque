from typing import List
from pydantic import BaseModel

class SupplierRequest(BaseModel):
    cnpj:str
    razao_social:str
    nome_fantasia:str
    endereco:str
    telefone: List[str]
