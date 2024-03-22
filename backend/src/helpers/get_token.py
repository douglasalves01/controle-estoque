from fastapi import Request, HTTPException

def get_token(request: Request):
    if not request.headers.get("authorization"):
        raise HTTPException(status_code=422, detail="Acesso Negado!")
    auth_header = request.headers.get("authorization")
    if auth_header is None:
        return None
    token = auth_header.split(" ")[1]
    return token if token else None
