

from fastapi import FastAPI 
from routers.products import router as producto_router


app = FastAPI()
app.include_router(producto_router)



