from fastapi import FastAPI
from routes.categoryRoutes import routerCategory
from routes.userRoutes import routerUser
from database.conn import conn

app=FastAPI()
connection=conn
app.include_router(routerCategory)
app.include_router(routerUser)