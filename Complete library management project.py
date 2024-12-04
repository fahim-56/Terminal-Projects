class Book:
    def __init__(self,catagory,name,id,quantity):
        self.id = id
        self.name = name
        self.catagory = catagory
        self.quantity = quantity

class User:
    BorrowedBookList =[]
    def __init__(self,name,id,password):
        self.password = password
        self.id = id
        self.name = name

class library:
    users = []
    def __init__(self,name,owner):
        self.name = name
        self.owner = owner
        self.books = []

    def addbook(self,catagory,name,id,quantity):
        book = Book(catagory,name,id,quantity)
        self.books.append(book)
        print(f"\n\t{book.name} added successfully !")

    def adduser(self,name,id,password):
        user = User(name,id,password)
        self.users.append(user)
        return user

    def borrow_book(self,username,id,password,Book_id):
        user = User(username,id,password)
        
        for bk in self.books:
            if bk.id == Book_id:
                if bk in user.BorrowedBookList:
                    print("\n\tAlready Borrowed.")
                    return
                elif bk.quantity < 1:
                    print("\n\tBooks are not available in copies")
                    return
                else:
                    user.BorrowedBookList.append(bk)
                    for x in user.BorrowedBookList:
                        print(x.name)
                    bk.quantity -= 1
                    print(f"\n\t{bk.name} Successfully borrowed")
                    return
        print("\n\tBook Not found.")

    def returnBook(self,bookid):
        flag = False
        for bk in self.books:
            if bk.id == bookid:
                bk.quantity += 1
                flag = True
        if(flag == False):
            print("This is not the book from our library...")


library1 = library("Islamic Library","Fahim")
admin = library1.adduser("Fahim",10,"Fahim")
user1 = library1.adduser("Tonmoy",11,"Tonmoy")
book1 = library1.addbook("Tafseer","Tafseer Ibn kasir",3001,2)


current_user = admin
while True:
    if current_user == None:
        print("\tNo loged in user.")
        op = (input("\n\tLog in ? Registration (l/r)\n"))
        
        if op =='r':
            id = int(input("\n\tEnter id: "))
            name = input("\n\tEnter name : ")
            password = input("\n\tEnter password : ")
            u = library1.adduser(name,id,password)
            current_user = u

        elif op =='l':
            id = int(input("\n\tEnter id: "))
            password = input("\n\tEnter password : ")
            match = False
            for user in library1.users:
                if user.id == id and user.password == password:
                    current_user = user.name
                    match = True
                    break
            if match == False:
                print(f"\n\tNo user found !")
    elif current_user == admin :
        op = int(input("""Choose option:
            1.Add book
            2.Add user
            3.Show user
            4.Show books
            5.Log out\n"""))
        
        if op ==1:
            id = int(input("\n\tEnter id: "))
            name = input("\n\tEnter Book name : ")
            catagory = input("\n\tEnter catagory : ")
            quantity = int(input("\n\tEnter quantity : "))
            library1.addbook(catagory,name,id,quantity)

        elif op == 2:
            username = input("Enter Your name : \n")
            userid = int(input("Enter Your id : \n"))
            userpass = input("Enter Your password : \n")
            library1.adduser(username,userid,userpass)


        elif op == 3:
            print("\n\nMembers List :\n\n")
            for user in library1.users:
                print(user.id,end = " ")
                print(user.name)

        elif op == 4:
            print("\n\n Book List :\n\n")
            for book in library1.books:
                print(book.id ,end =" ")
                print(book.name ,end =" ")
                print(book.quantity ,end =" piece \n")

        elif op ==5:
            current_user = None
            print("Successfully loged out...")
    else:
        op = int(input("""Choose option:
            1.Show book
            2.Borrow book
            3.Return Book
            4.Previous Borrowed Book list
            5.Log out\n"""))
        if op == 1:
            for book in library1.books:
                print(book.id ,end =" ")
                print(book.name ,end =" ")
                print(book.quantity ,end =" piece \n")

        elif op ==2:
            username = input("Enter Your name : \n")
            userid = int(input("Enter Your id : \n"))
            userpass = input("Enter Your password : \n")
            flag = False
            for us in library1.users:
                if userid == us.id and userpass == us.password:
                    Bookid = int(input("Enter the book id you want to borrow : \n"))
                    library1.borrow_book(username,userid,userpass,Bookid)
                    flag = True
            if(flag == False):
                print("Wrong Information !\n")

                
        elif op ==3:
            bookid = input("\nEnter book id :")
            library1.returnBook(bookid)

        elif op ==4:
            username = input("Enter Your name : \n")
            userid = input("Enter Your id : \n")
            userpass = input("Enter Your password : \n")
            for x in user.BorrowedBookList:
                print(x.name)

        elif op ==5:
            current_user = None
