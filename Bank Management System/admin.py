from datetime import datetime
class User:
    def __init__(self,name,password):
        self.name = name
        self.password = password
        self.balance = 0

# Admin = admin("Admin","admin")

class admin(User):
    def __init__(self, name, password):
        super().__init__(name, password)

    def create_account(self,name,email,address,account_type,password,bank):
        account = account_user(name,email,address,account_type,password,bank)
        bank.accounts.append(account)
        print("Account created successfully!")

    def delete_account(self,account,bank):
        bank.accounts.remove(account)
        print(f"{bank.name}'s account deleted successfully!")


class account_user(User):
    def __init__(self, name, email, address, account_type, password,bank):
        self.email = email
        self.address = address
        self.account_type = account_type
        self.balance = 0
        self.account_number = len(bank.accounts)+1000
        self.histry = []
        self.loan_taken = 0
        super().__init__(name, password)

    def diposite(self,amount,bank):
        self.balance += amount
        bank.Total_balance +=amount
        print(f"Diposited {amount} taka at {datetime.now()}. \nCurrent balance : {self.balance}")
        self.histry.append(f"Diposited {amount} taka at {datetime.now()}. \nCurrent balance : {self.balance}")

    def widthdraw(self,amount,bank):
        if bank.Total_balance == 0:
            print("Bank is Bankrupt.")
            return
        if self.balance < amount :
            print("Withdrawal amount exceeded")
            return
        self.balance-=amount
        bank.Total_balance -=amount
        print(f"Widthdraw {amount} taka at {datetime.now()}. \nCurrent balance : {self.balance}")
        self.histry.append(f"Widthdraw {amount} taka at {datetime.now()}. \nCurrent balance : {self.balance}")
        return amount
    
    def check_transaction_history(self):
        for x in self.histry:
            print(x)
    
    
    def check_balance(self):
        print(f"Your available balance is {self.balance} Taka.")
        return self.balance
    
    def take_loan(self,amount,bank):
        if bank.loan_giving_permission == False:
            print("Loan is not availabe now")
            return 
        if self.loan_taken >= 2:
            print("Your loan limit is over.")
            return
        self.balance += amount
        bank.Total_balance -=amount
        bank.Total_Loan += amount
        print(f"{amount} taka added to your account as loan.")
        self.histry.append(f"You take loan {amount} taka at {datetime.now()}")
        self.loan_taken += 1

    def transfer_balance(self,amount,account,bank):
        if amount > self.balance:
            print("Your account has not sufficient balance.")
            return
        if account in bank.accounts:
            account.balance += amount
            self.balance -= amount
            print(f"{amount} Taka transfered to {account.name}'s account successfully at {datetime.now()}!")
            self.histry.append(f"{amount} transfered to {account.name}'s account successfully at {datetime.now()}!")
            return
        print("Account not found!")