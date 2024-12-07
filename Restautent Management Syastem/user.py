from abc import ABC
from item import item
from order import Order

class user(ABC):
    def __init__(self, name, email, phone, address):
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address

class employee(user):
    def __init__(self, name, email, phone, address, designation, salary):
        super().__init__(name, email, phone, address)
        self.designation = designation
        self.salary = salary

class admin(user):
    def __init__(self, name, email, phone, address,password):
        super().__init__(name, email, phone, address)
        self.password = password

    def add_employee(self, restaurent, employee):
        restaurent.add_employee(employee)
    
    def view_employee(self,restaurent):
        restaurent.view_employee()
    
    def add_food_item(self,restaurent,item):
        restaurent.Menu.add_item(item)

    def delete_food_item(self,restaurent,item_name):
        restaurent.Menu.remove_item(item_name)
    
    def view_menu(self,restaurent):
        restaurent.Menu.show_item()

class customer(user):
    def __init__(self, name, email, phone, address):
        super().__init__(name, email, phone, address)
        self.cart = Order()

    def view_menu(self,restaurent):
        restaurent.Menu.show_item()
    
    def add_to_cart(self,restaurent,item_name,quantity):
        it = restaurent.Menu.find_item(item_name)
        if it:
            if quantity > it.quantity:
                print("Quantity Exceeded.")
            it.quantity -= quantity 
            itm = item(it.name,it.price,quantity)
            self.cart.add_item(itm)
            print(f"{quantity} {item_name} added to cart successfully!")
        else:
            print("Item not found!")

    
    def view_cart(self):
        print("     **View cart**")
        print("Name\tPrice\tQuantity")
        for item,quantity in self.cart.items.items():
            print(f"{item.name}\t{item.price}\t{item.quantity}")
        print(f"Total Price : {self.cart.total_price()}")
    
    def pay_bill(self,amount):
        if amount == self.cart.total_price():
            print("Thanks for paying bill...")
            self.cart.clear()
        elif amount > self.cart.total_price():
            print(f"{self.cart.total_price()} Paid Successfully")
            print(f"Your remaining {amount - self.cart.total_price()} Taka")
            self.cart.clear()
        else:
            print(f"Your have to pay {self.cart.total_price() - amount} Taka more...")
            