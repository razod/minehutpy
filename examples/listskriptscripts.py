from minehut import minehut

m = minehut()

TOKEN = "token"
SESSIONID = "sessionid"
SERVERID = "serverid"

def listSkriptScripts(token, session, server_id):
    return m.listFileDir(token, session, server_id, "plugins/Skript/scripts")

print(listSkriptScripts(TOKEN, SESSIONID, SERVERID))