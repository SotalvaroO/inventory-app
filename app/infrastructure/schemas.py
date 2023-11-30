def individual_serial(product) -> dict:
    return {
        "product_sku" : product["sku"],
        "name" : product["name"],
        "description" : product["description"],
        "price" : product["price"],
        "stock" : product["stock"],
        "thumbnail" : product["thumbnail"],
    }
    
    def list_serial(products) -> list:
        return [individual_serial(product) for product in products]