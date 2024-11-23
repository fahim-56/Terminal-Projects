class product:
    product_list = []

    def __init__(self):
        pass
       
    def add_to_list(self,name,price_per_unit,total_quantity):
        self.name = name
        self.price_per_unit = price_per_unit
        self.total_quantity = total_quantity

        self.product_list.append({"name":self.name,"price":self.price_per_unit,"quantity":self.total_quantity})

class shope(product):

    cart = []

    def __init__(self):
        super().__init__()

    def Add_to_cart(self,item,quantity):
        self.item = item
        self.quantity = quantity
        flag = True
        for product in self.product_list:
            if(product["name"] == self.item ):
                flag = False
                if(product["quantity"]>=self.quantity ):
                    self.cart.append({"item": product["name"],"price": (self.quantity * product["price"] )})
                    product["quantity"] -= self.quantity
                    print(f"{self.quantity} unit {product["name"]} added to cart..")
                else:
                    print(f"Sorry, {product["quantity"]}  unit  {product["name"]} is available just.")
        if(flag):
            print("The Product is not available here.")

    def Remove_the_last_item_From_cart(self):
        self.cart.pop()

    def checkout(self):
        Total_price = 0
        for x in self.cart:
            Total_price += x["price"]

        self.cart.clear()
        print(f'\nPlease pay {Total_price} Taka')

    

# Include product into shop
 
products = product()
products.add_to_list("Sugar",120,20)
products.add_to_list("Salt",40,10)
products.add_to_list("Rice",70,50)
products.add_to_list("Oil",180,5)
products.add_to_list("Harpic",120,30)

# while True:
#     x = int(input("""1.Add more
#     2. Exit\n"""))
#     if(x==2):
#         break
#     Str = input("Enter your product name,price per unit and quantity : ")
#     price = int(input())
#     amount = int(input())
#     products.add_to_list(Str,price,amount)


# shoping

customer = shope()
# customer.Add_to_cart("Sugar",5)
# customer.Add_to_cart("Rice",10)
# customer.Add_to_cart("Salt",10)
# customer.Add_to_cart("Salt",10)
# customer.Add_to_cart("Oil",10)
# customer.Add_to_cart("Egg",10)

print("Start to add in cart\n")
while True:
    x = int(input("""1.Add more
    2. Exit\n"""))
    if(x==2):
        break
    print("Enter your product name and quantity : \n")
    Str = input()
    quantity = int(input())
    customer.Add_to_cart(Str,quantity)

# customer.Remove_the_last_item_From_cart()
customer.checkout()
