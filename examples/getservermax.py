from minehut import minehut
import json

m = minehut()

def getServerMaxPlayers(srv):
    j = json.dumps(m.getServerByName(srv))
    jso = json.loads(j)
    return jso["server"]['maxPlayers']

getServerMaxPlayers("warzone")