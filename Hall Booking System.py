class Hall:
    def __init__(self,row,collum,hall_no):
        self.seats = {}
        self.show_list = []
        self.row = row
        self.collum = collum
        self.hall_no = hall_no

    def entry_show(self, show_id, movie_name , time):
        show = show_id, movie_name, time
        self.show_list.append(show)
        self.seats[show_id] = [[0 for x in range (self.collum)] for x in range(self.row)]
        print(f"{movie_name} added to show list successfully!")

    def book_seat(self,show_id,seat):
        if show_id not in self.seats:
            print(f"Show ID {show_id} does not exist.")
            return

        for x in seat:
            if(x[0]>=self.row or x[1] >=self.collum):
                print("Invalid seat!")

            if self.seats[show_id][x[0]][x[1]] == 0:
                self.seats[show_id][x[0]][x[1]] = 1
                print(f"Your {x} number seat booked, Successfully!")
            else:
                print(f"{x} number seat already booked.")

    def view_show_list(self):
        for x in self.show_list:
            print(x)

    def  view_available_seats(self,show_id):

        if show_id not in self.seats:
            print(f"Show ID {show_id} does not exist.")
            return
        print(f"Available seats for show {show_id}:")
        for x in range(self.row):
            for y in range(self.collum):
                if self.seats[show_id][x][y] == 0:
                    print("A",end=" ")
                elif self.seats[show_id][x][y] == 1:
                    print("B",end=" ")
            print()

    def cancel_booking(self,show_id,seat):
        if show_id not in self.seats:
            print(f"Show ID {show_id} does not exist.")
            return
        for x in seat:
            if(x[0]>=self.row or x[1] >=self.collum):
                print("Invalid seat!")

            if self.seats[show_id][x[0]][x[1]] == 1:
                self.seats[show_id][x[0]][x[1]] = 0
                print(f"Your {x} number seat canceled, Successfully!")
            else:
                print(f"{x} number seat is not booked.")

    users = []

    def adduser(self,user):
        self.users.append(user)
        print(f"{user.name} added to user list,Successfully!")

class User:
    def __init__(self,name,password):
        self.name = name
        self.password = password

hall = Hall(5,5,101)
hall.entry_show(101,"The Massage!","12-5-2024")
admin = User("Fahim","Fahim")
hall.adduser(admin)
user = None
while(True):
    if user == None:
        print("\tNo loged in user.")
        op = (input("\n\tLog in ? Registration (l/r)\n"))
        
        if op =='r':
            name = input("\n\tEnter name : ")
            password = input("\n\tEnter password : ")
            us = User(name,password)
            u = hall.adduser(us)
            user = us.name

        elif op =='l':
            name = input("\n\tEnter name : ")
            password = input("\n\tEnter password : ")
            match = False
            for us in hall.users:
                if us.name == name and us.password == password:
                    user = us.name
                    match = True
                    break
            if match == False:
                print(f"\n\tNo user found !\n")
    elif user == admin.name :
        password = input("         Confirm admin password : ")
        if(password == admin.password):
            op = int(input("""Choose a Option
                1.Add Show
                2.Veiw Shows
                3.Veiw available seat
                4.Add User
                5.Veiw user
                6.Log Out       \n"""))
            if(op==1):
                __id = int(input("Enter show id :"))
                __show_name = input("Enter show name :")
                __show_time = input("Enter show time :")
                hall.entry_show(__id,__show_name,__show_time)

            elif(op==2):
                print("Todays availabe shows are : ")
                hall.view_show_list()
                
            elif(op==3):
                id = int(input("Enter show id :\n"))
                hall.view_available_seats(id)

            elif(op==4):
                name = input("Enter user name :")
                password = input("Enter user password :")
                u =User(name,password)
                hall.adduser(u)

            elif(op==5):
                print("List of users are : \n")
                for x in hall.users:
                    print(x.name," ")

            elif(op==6):
                print("Loged Out,Successfully !.\n")
                user = None
        else:
            print("Wrong password.\n")
            user = None

    else:
        op = int(input("""Choose a Option
            1.Veiw Shows
            2.Veiw available seat
            3.Book Seat
            4.Cancel Seat
            5.Log Out       \n"""))
        if(op==1):
            print("Todays availabe shows are : ")
            hall.view_show_list()
        elif(op==2):
            id = int(input("Enter show id :\n"))

            hall.view_available_seats(id)
        elif(op==3):
            show_id = int(input("Enter the show id : "))
            seat_no = int(input("Enter the number of seats :"))
            seat =()
            for i in range(seat_no):
                row = int(input("Enter the row of seat : "))
                col = int(input("Enter the col of seat : "))
                seat += ([row,col],)
            hall.book_seat(show_id,seat)
        elif(op==4):
            show_id = int(input("Enter the show id : "))
            seat_no = int(input("Enter the number of seats :"))
            seat =()
            for i in range(seat_no):
                row = int(input("Enter the row of seat : "))
                col = int(input("Enter the col of seat : "))
                seat += ([row,col],)
            hall.cancel_booking(show_id,seat)
            
        elif(op==5):
            print("Loged Out,Successfully !.")
            user = None

