from menu import menu
class restaurent:
    def __init__(self,name):
        self.name = name
        self.employees = []
        self.Menu = menu()

    def add_employee(self,employee):
        self.employees.append(employee)
        print(f"{employee.name} added successfully to employee list. ")

    def view_employee(self):
        print("Emplyees list :")
        print("Name\tEmail\tPhone\tAddress\tDesignation\tSalary")
        for emp in self.employees:
            print(emp.name,emp.email,emp.phone,emp.address,emp.designation,emp.salary)
