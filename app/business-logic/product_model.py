
from typing import List
from pydantic import BaseModel


class Product(BaseModel):
    product_sku : str
    name : str
    description : str
    price : int
    stock : int
    thumbnail : str
    
class ProductDetail(BaseModel):
    product_sku : str
    name : str
    description : str
    price : int
    stock : int
    images : List[str]