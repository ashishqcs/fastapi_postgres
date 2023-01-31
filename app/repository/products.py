from sqlalchemy.orm import Session
from app.schemas import product, request


def get_product(db: Session, id: int):
    return db.query(product.Product).get(id)


def get_all_products(db: Session):
    return db.query(product.Product).all()


def create_product(db: Session, req_product: request.Product):
    db_product = product.Product(id=req_product.id, name=req_product.name, price=req_product.price)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)


