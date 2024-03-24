from fastapi import FastAPI
from routes.categoryRoutes import routerCategory
from routes.userRoutes import routerUser
from routes.supplierRoutes import routerSupplier
from database.conn import conn

app=FastAPI()
connection=conn
app.include_router(routerCategory)
app.include_router(routerSupplier)
app.include_router(routerUser)