from json import *


def get_all_projects():
    with open('products.txt', 'r') as products_file:
        return [loads(line.strip()) for line in products_file]
