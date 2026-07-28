

from models import Product
from config import product_collection



def get_products():
    products = []

    for product in product_collection.find({}, {"_id": 0}):
        products.append(Product(**product))

    return products



def get_product(id: int):
    product = product_collection.find_one(
        {"Id": id},
        {"_id": 0}
    )

    if product:
        return Product(**product)

    return None



def create_product(product: Product):
    product_collection.insert_one(product.model_dump())
    return product



def update_product(id: int, updated_product: Product):
    result = product_collection.update_one(
        {"Id": id},
        {"$set": updated_product.model_dump()}
    )

    if result.modified_count > 0:
        return updated_product

    return None


# Delete a product
def delete_product(id: int):
    product = product_collection.find_one(
        {"Id": id},
        {"_id": 0}
    )

    if product:
        product_collection.delete_one({"Id": id})
        return Product(**product)

    return None



