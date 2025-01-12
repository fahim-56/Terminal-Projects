from bank import Bank
from user import account_user,admin

IBBL = Bank("Islami Bank",10000000)
Admin = admin("Admin","admin")
IBBL.accounts.append(Admin)
current_user = None
while True:
    if current_user == None:
        print("\tNo loged in user.")
        op = (input("\n\tLog in ? Registration (l/r)\n"))
        if op =='r':
            name = input("Enter your name:")
            email = input("Enter your email:")
            address = input("Enter your address:")
            account_type = input("Enter your account type:")
            password = input("Enter your password:")
            account = account_user(name,email,address,account_type,password,IBBL)
            IBBL.accounts.append(account)
            current_user = account
        elif op == 'l':
            x=(input("\n\tUser log in ? Admin Log in (u/a)\n"))
            if(x=='a'):
                name = input("Enter Admin name:")
                password = input("Enter Admin password:")
                user = IBBL.find_account(name)
                if user == None:
                    print()
                elif user.password != password:
                    print("Wrong password")
                else:
                    current_user = user

                if current_user == Admin:
                    print("Successfully loged in as admin!")
                else:
                    print("You are not Admin.")
                    current_user = None
            elif x=='u':
                name = input("Enter your name:")
                password = input("Enter your password:")
                user = IBBL.find_account(name)
                if user == None:
                    print("User not found!")
                elif user.password != password:
                    print("Wrong password")
                else:
                    current_user = user
                    print("Loged in successfully!")
    elif current_user == Admin:
        op = int(input("""Enter your option
                       1.Create account
                       2.Delete account
                       3.Veiw user account list
                       4.Veiw total balance in bank
                       5.Check total loan amount
                       6.Loan giving permission
                       7.Log out
                       """))
        if op == 1:
            name = input("Enter User name:")
            email = input("Enter User email:")
            address = input("Enter User address:")
            account_type = input("Enter User account type:")
            password = input("Enter User password:")
            Admin.create_account(name,email,address,account_type,password,IBBL)
        elif op == 2:
            name = input("Enter the account name you want to delete :")            
            account = IBBL.find_account(name)
            Admin.delete_account(account,IBBL)
            
        elif op == 3:
            for x in  IBBL.accounts:
                print(x.name)
        elif op == 4:
            print(IBBL.Total_balance)
        elif op == 5:
            print(IBBL.Total_Loan)
        elif op == 6:
            x = int(input("""Loan giving permission
                          1.on
                          2.off
                          """))
            if x==1:
                IBBL.loan_giving_permission =True
                print("Loan giving permission is on now.")
            elif x==2:
                IBBL.loan_giving_permission = False
                print("Loan giving permission is off now.")
            else:
                print("Wrong input.")
        elif option ==7:
            current_user = None
        else:
            print("Wrong option chossen!")

    else:
        option = int(input("""Enter your option
                       1.Diposite Balance
                       2.Widthdraw Balance
                       3.Check Balnce
                       4.Transection Histroy
                       5.Take loan
                       6.Transfer Balance
                       7.Log out
                       """))
        if option ==1:
            amount = int(input("Enter diposite amount:"))
            account.diposite(amount,IBBL)
        elif option == 2:
            amount = int(input("Enter widthdraw amount:"))
            account.widthdraw(amount,IBBL)
        elif option == 3:
            account.check_balance()
        elif option == 4:
            account.check_transaction_history()
        elif option == 5:
            amount = int(input("Enter loan amount:"))
            account.take_loan(amount,IBBL)
        elif option == 6:
            amount = int(input("Enter the amount to transfer:"))
            receiver_name = input("Enter Receiver Account name :")
            receiver = IBBL.find_account(receiver_name)
            account.transfer_balance(amount,receiver,IBBL)
        elif option ==7:
            current_user = None
        else:
            print("Wrong option chossen!")
# r
# Fahim
# fahim@gmail.com
# Rajbari
# Current
# 1234
# 7
# r
# Tonmoy
# tonmoy@gmail.com
# Dhaka
# Savings
# 123