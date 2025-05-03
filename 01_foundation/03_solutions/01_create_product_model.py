from pydantic import BaseModel

class Product(BaseModel):
    id: int
    name: str
    price: float
    in_stock: bool = True

input_data = {'id': 201, 'name': 'Laptop', 'price': 50000.0, 'in_stock': True}

model = Product(**input_data)
print(model)