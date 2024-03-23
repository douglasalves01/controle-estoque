from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from roles.user import verifyAccess
from helpers.check_token import checkToken
def check_token_and_verify_access(nivel_description):
    def decorator(func):
        async def wrapper(request: Request):
            token = checkToken(request)
            if(verifyAccess(request, nivel_description)):
                return 'acesso liberado'
            return await func(request, token)
        return wrapper
    return decorator
