from pydantic import BaseModel

class SupplierRequest(BaseModel):
    CNPJ:str
    razao_social:str
    nome_fantasia:str
    endereco:str
    telefone:str
