from fastapi import Request

def get_token(request: Request):
    auth_header = request.headers.get("authorization")
    if auth_header is None:
        return None
    token = auth_header.split(" ")[1]
    return token if token else None
