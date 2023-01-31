from fastapi import FastAPI
from .routers import product_router

app = FastAPI()

app.include_router(product_router.router)


@app.get("/")
def root():
    return "fastapi service is up."
