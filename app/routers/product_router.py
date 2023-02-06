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


@router.post("/")
def product(req_product: request.Product, db: Session = Depends(get_db)):
    products.create_product(db, req_product)


@router.get("/{product_id}")
def product(product_id: int, db: Session = Depends(get_db)):
    return products.get_product(db, product_id)


@router.get("/all/")
def get_products(db: Session = Depends(get_db)):
    return products.get_all_products(db)

