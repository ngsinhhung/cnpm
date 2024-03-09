import json

def load_categories():
    with open('data/categories.json', encoding='utf-8') as file:
        return json.load(file)

def load_products(q=None, category_id=None):
    with open('data/products.json', encoding='utf-8') as file:
        products = json.load(file)
        if q:
            products = [p for p in products if p['name'].find(q) >= 0]
        if category_id:
            products = [p for p in products if p['category_id'].__eq__(int(category_id))]
        return products

def load_product_detail(product_id=None):
    with open('data/products.json', encoding='utf-8') as file:
        product = json.load(file)
        return [p for p in product if p['id'].__eq__(int(product_id))]