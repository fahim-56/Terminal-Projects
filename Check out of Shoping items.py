class customer:
    def __init__(self,customer_name):
        self.customer_name = customer_name
        self.cart =[]

    def add_to_cart(self,item,price,quantity):
        product = {'item':item ,'price':price,'quantity':quantity}
        self.cart.append(product)

    def total_to_pay(self):
        total=0
        for item in self.cart:
            total+=(item['price']*item['quantity'])
        return total

    def checkout(self,amount):
        if(self.total_to_pay()>amount):
            print("Total: ",self.total_to_pay())
            print(f"Please provide {self.total_to_pay()-amount} more")
            return
        print("Total: ",self.total_to_pay())
        print(f"Here is Your Reminder {amount - self.total_to_pay()}")
        return amount - self.total_to_pay()

customer1 = customer(1001)
customer1.add_to_cart('Biskit',80,2)
customer1.add_to_cart('Cake',500,1)
customer1.add_to_cart('Ice cream',50,5)


# customer1.total_to_pay()
N= int(input("Please pay your amount:"))
customer1.checkout(N)