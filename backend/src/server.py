from fastapi import FastAPI
from routes.categoryRoutes import routerCategory
from routes.userRoutes import routerUser
from routes.supplierRoutes import routerSupplier
from routes.productRoutes import routerProduct
from routes.saleRoutes import routerSale
from routes.stockRoutes import routerStock
from routes.reportsRoutes import routerReports
from database.conn import conn
from swagger_ui import api_doc
app = FastAPI()

connection=conn
app.include_router(routerCategory)
app.include_router(routerSupplier)
app.include_router(routerUser)
app.include_router(routerProduct)
app.include_router(routerSale)
app.include_router(routerStock)
app.include_router(routerReports)
#documentação da api
api_doc(app, config_path='./swagger.json', url_prefix='/api/doc', title='API doc')