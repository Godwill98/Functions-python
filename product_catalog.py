
class product:
    def __init__(self,name,price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def total_quantity(self):
        return self.price * self.quantity

product1 = product("Laptop", 1200, 3)
product2 = product("Phone", 800, 2)

print(f"THE total qunatitiies of product {product1.name} is {product1.total_quantity()}")

