from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas import product, request
from app.repository import products
from app.config.database import SessionLocal

router = APIRouter(
    prefix="/products",
    tags=["products"]
)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


#
# products = [
#     Product(code="A1", name="iphone 12", price=500),
#     Product(code="A2", name="redmi", price=100)
# ]


# @router.get("/all")
# def get_products(db: Session = Depends(get_db)):
#     return products.get_all_products(db)


@router.post("/")
def get_products(req_product: request.Product, db: Session = Depends(get_db)):
    products.create_product(db, req_product)

