class bank_account:
    
    bank_name = "Islami Bank"

    def __init__(self,starting_amount):
        if starting_amount<1000:
            print(f"Insufficient Balance")
            return 
        self.balance = starting_amount
        print(f"Welcome to our bank. Your current balance is {self.balance}")
        self.max_withdraw = 1000000
        self.min_withdraw = 1000

    def diposite(self,amount):
        self.balance += amount
        print(f"New Blance {self.balance}")

    def widthdaw(self,amount):
        if amount < self.min_withdraw:
            print(f"Your amount is less then minimum amount to withdraw")
        
        elif amount > self.max_withdraw:
            print(f"Your amount cross the maximum amount limit to withdraw")

        elif self.balance - amount < 1000:
            print("Insufficinet balance.")

        else:
            self.balance -= amount
            print(f"Your current Balance is {self.balance}")

    def balance_check(self):
        print(f"Your current balance is {self.balance}")


print("Enter the amount You want to start with:")
N = int(input())
myAccount = bank_account(N)


while(True): 
    
    i = int(input(f"""Enter your choice:
                1. diposite 
                2. withdraw
                3. check balance
                4. exit\n"""))     
    if i==1:
        print("Enter the diposite amount :")
        N = int(input())
        myAccount.diposite(N)

    elif i==2:
        print("Enter the amount you want to withdraw:")
        N = int(input())
        myAccount.widthdaw(N)

    elif i==3:
        myAccount.balance_check()

    elif i==4:
        print("Thanks for using our service.")
        break
    
    else:
        print("Wrong Input")
        break
