from minehut import minehut
import json

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

def getServerMaxPlayers(srv):
    j = json.dumps(m.getServerByName(srv))
    jso = json.loads(j)
    print(jso["server"]['maxPlayers'])

def main():
    # login()
    # getServers()
    getServerMaxPlayers("warzone")

main()