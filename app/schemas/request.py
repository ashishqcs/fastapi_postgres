from pydantic import BaseModel


class Product(BaseModel):
    id: int
    name: str
    price: float

    class Config:
        orm_mode = True
