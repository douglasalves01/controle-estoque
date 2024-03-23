from pydantic import BaseModel
# from typing import Optional

class UserRequest(BaseModel):
    name: str
    password:str
    id_nivelacesso: str = ""