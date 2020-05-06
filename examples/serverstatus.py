from minehut import minehut

token = "YOUR_MH_TOKEN"
sessionid = "YOUR_MH_SESSIONID"
serverid = "YOUR_MH_SERVERID"

m = minehut()

print(m.getServerStatus(token, sessionid, serverid))