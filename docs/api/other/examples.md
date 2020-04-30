# Examples

Here a few examples you can use to help yourself.

# Login through command line.
```python
from minehut import minehut

m = minehut()

def login():
    email = str(input("email? "))
    password = str(input("password? "))
    print(m.userLogin(email, password))

login()
```

# Get the max players of a server
```python
from minehut import minehut
import json

m = minehut()

def getServerMaxPlayers(srv):
    j = json.dumps(m.getServerByName(srv))
    jso = json.loads(j)
    return jso["server"]['maxPlayers']

print(getServerMaxPlayers("warzone"))
```