from pydantic import BaseModel

class ConfigRequest(BaseModel):
    margem_lucro: str
    comissao_venda: str
    custo_fixo:str
