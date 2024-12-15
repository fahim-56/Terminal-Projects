class Bank:
    
    def __init__(self,bank_name,Total_balance):
        self.bank_name = bank_name
        self.Total_balance = Total_balance
        self.Total_Loan = 0
        self.loan_giving_permission = True
        self.accounts = []

    def find_account(self,name):
        for x in self.accounts:
            if x.name == name:
                return x
        return