from fastapi import FastAPI
from routes.categoryRoutes import routerCategory

app=FastAPI()

app.include_router(routerCategory)