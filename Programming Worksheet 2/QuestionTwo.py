# Shop Program
class Product:
    def __init__(self,name,price,stock):
        self.name = name
        self.price = price
        self.stock = stock
    def display_products(self,number):
        print(f"{number}. {self.name}| price: {self.price}| stock: {self.stock}")
    def sell(self,quantity):
        if quantity > self.stock:
            print("Sorry, you don't have enough stock to sell")
        else:
            self.stock -= quantity
            print(f"Product sold!")
        return quantity

# Storing of Products
products = []
product_number = int(input("Enter the number of products you want to store: "))
for i in range(product_number):
    product_name = input(f"Enter product with index {i+1} name: ")
    product_price = int(input("Enter product price: "))
    product_stock = int(input("Enter product stock: "))
    products.append(Product(product_name,product_price,product_stock))
# Menu
print("Enter 1 to sell products")
print("Enter 2 to display total sales and remaining stock")

while True:
    choice = int(input("Enter your choice: "))
    if choice == 1:
        x = 0
        for product in products:
            x+=1
            product.display_products(x)
        product_id = int(input("Enter product ID you want to sell: "))
        quantity_sell = int(input("Enter quantity to sell: "))
        for index,i in enumerate(products):
            if (index+1) == product_id:
                i.sell(quantity_sell)
                break
            else:
                print("Enter appropriate ID")
    elif choice == 2:
        x = 0
        for product in products:
            x+=1
            product.display_products(x)
        break






