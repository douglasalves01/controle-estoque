from pydantic import BaseModel

class UserRequest(BaseModel):
    name: str
    password:str