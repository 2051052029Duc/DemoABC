import json
from DemoSaleApp import app


# def load_categories():
#     with open(f'{app.root_path}\data\categories.json', encoding='utf-8') as f:
#         return json.load(f)

def load_products():
    with open(f'{app.root_path}\data\products.json', encoding='utf-8') as f:
        return json.load(f)