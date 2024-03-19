from fastapi import FastAPI
from routes.categoryRoutes import routerCategory
from database.conn import conn

app=FastAPI()
connection=conn
app.include_router(routerCategory)