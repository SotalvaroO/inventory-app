from fastapi import APIRouter

routes = APIRouter(prefix= '/products', tags=['Product'],)

@routes.get('/')
def get_products_by_name(name: str = ""):
    return [
        {
            "name" : "Iphone"
        }
    ]
    
@routes.get('/{sku}/detail')
def get_product_detail_by_sku(sku:str):
    return {
        "name": "Iphone"
    }
    
@routes.post('/')
def create_product(product:object):
    return product

@routes.put('/{sku}')
def update_product(id:str, product):
    return {
        "id":id,
        "product": product
    }
    
@routes.delete('/{sku}')
def delete_product_by_sku(sku: str):
    return {
        "sku":sku
    }