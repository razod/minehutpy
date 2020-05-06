from minehut import minehut

m = minehut()

def login():
    email = str(input("email? "))
    password = str(input("password? "))
    print(m.userLogin(email, password))

login()