from minehut import minehut

m = minehut()

def login():
    email = str(input("email? "))
    password = str(input("password? "))
    print(m.userLogin(email, password))

def getServers():
    print(m.getServers())

sessionid = "my x-session-id"
token = "my token"
serverid = "my server id"

def getServer(srv):
    print(m.getServerByName(srv))

def main():
    # login()
    # getServers()
    getServer("warzone")

main()