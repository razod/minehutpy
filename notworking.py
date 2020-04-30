import json
import requests

# this is a list of the currently not working api endpoints

class notworking():
    def __init__(self):
        pass
    def listRootFiles(self, token, xsessionid, server_id):
        headers = {
            'content-type': 'application/json; charset=utf-8',
            'x-session-id': xsessionid,
            'Authorization': token
        }
        url = "https://api.minehut.com/file/" + server_id + "/list"
        response = requests.get(url, headers=headers ,verify=False)
        j = json.loads(response.content)
        return j