#object oriented
    #(1)python class
#when we write funtion in a class, it called method
#when we write variable in class, it called attribute
class User:
    name = ''
    email = ''
    password = ''
    login = False

    def login(self):
        email= input("enter email: ")
        password= input("enter password: ")

        if email == self.email and password == self.password:
            login = True
            print("login successfull!!")
        else:
            print("login failed!!")

#use of constructor
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password



    def logout(self):
        login = False
        print("logged out!")

    def isLoggedIn(self):
        if self.login:
            return True
        else:
            return False

    def profile(self):

        if self.isLoggedIn():
            print(self.name, "\n", self.email)

        else:
            print("user is not logged in")
#make an object of a class
user1= User("Maynul islam", "maynulislam3", "12345")

'''user1.name = "Maynul Islam"
user1.email= "maynulislam3"
user1.password= "12345"'''

user1.login()
user1.profile()

hello = input()

