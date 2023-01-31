from app.config.database import Base
from sqlalchemy import Float, Column, Integer, String


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    price = Column(Float)
