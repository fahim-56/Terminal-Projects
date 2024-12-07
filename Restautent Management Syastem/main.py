from item import item
from restaurent import restaurent
from user import employee,customer,admin

res = restaurent("Fahim's Restaurent")
Fahim = admin("Fahim","fahim@gamil.com","01991027456","dhaka","pass")
def customer_menu():
    name = input("Enter your name : ")
    email = input("Enter your email : ")
    phone = input("Enter your phone : ")
    address = input("Enter your address : ")

    cus = customer(name=name,email=email,phone=phone,address=address)

    while True:
        print(f"\n\t\tWelcome {cus.name}...!")
        choice = int(input("""
                Enter Your choice:
                1. Veiw menu
                2. Add to cart
                3. Veiw cart
                4. Pay Bill
                5. Log out 
                           """))
        if choice == 1:
            cus.view_menu(res)
        elif choice == 2:
            item_name = input("Enter item name :")
            quantity = int(input("Enter item quantity :"))
            cus.add_to_cart(res,item_name,quantity)
        elif choice == 3:
            cus.view_cart()
        elif choice == 4:
            amount = int(input("Please pay your amount:"))
            cus.pay_bill(amount)
        elif choice == 5:
            break
        else:
            print("Invalid input.")

def admin_menu():
    name = input("Enter your name : ")
    email = input("Enter your email : ")
    phone = input("Enter your phone : ")
    address = input("Enter your address : ")
    password = input("Enter admin password : ")
    if name !=Fahim.name:
        print("Wrong Admin name !")
        return
    elif password != Fahim.password:
        print("Wrong password !")
        return
   
    ad = admin(name=name,email=email,phone=phone,address=address,password=password)
    while True:
        print(f"\n\t\tWelcome {ad.name} as admin !")
        choice = int(input("""
                Enter Your choice:
                1. Veiw menu
                2. Add food item
                3. Delete food item
                4. Add employee
                5. Veiw employee 
                6. Log out
                           """))
        if choice == 1:
            ad.view_menu(res)
        elif choice == 2:
            item_name = input("Enter item name :")
            item_price = int(input("Enter item price :"))
            quantity = int(input("Enter item quantity :"))
            it = item(name=item_name,price=item_price,quantity=quantity)
            ad.add_food_item(res,it)
        elif choice == 3:
            item_name = input("Enter item name :")
            ad.delete_food_item(res,item_name)
        elif choice == 4:
            emp_name = input("Enter your name : ")
            emp_email = input("Enter your email : ")
            emp_phone = input("Enter your phone : ")
            emp_address = input("Enter your address : ")
            emp_des = input("Enter your Designation : ")
            emp_salary = input("Enter your salary : ")
            emp = employee(emp_name,emp_email,emp_phone,emp_address,emp_des,emp_salary)
            ad.add_employee(res,emp)
        elif choice ==5:
            ad.view_employee(res)
        elif choice == 6:
            break
        else:
            print("Invalid input.\n")

while True:
    choise = int(input("""
Enter your choise:
        1.Customer
        2.Admin
        3.Exit
                   """))
    if choise == 1:
        customer_menu()
    elif choise == 2:
        admin_menu()
    elif choise == 3:
        break
    else:
            print("Invalid input.")

# 2
# Fahim
# f
# j
# j
# pass
# 2
# kh
# 10
# 10
# 6
# 1
# f
# def
# defd
# def
# 2
# kh
# 2