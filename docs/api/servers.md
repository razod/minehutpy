# Servers
do stuff with servers.
if you don't know how to get your token or xsessionid, go to the [**faq**](api/other/faq)

`getServers()` - Get a list of all running minehut servers.

`getServerByID(server_id)` - Get information about a server by id.

`getServerByName(server_name)` - Get information about a server by name.

`createServer(token, xsessionid, server_name)` - Create a server.

`getServerData(token, xsessionid, server_id)` - Get server data of a server.

`getServerStatus(token, xsessionid, server_id)` - Get the status of a server (Starting, stopping, etc). 

`hibernationServerStart(token, xsessionid, server_id)` - Start a server when it is in hibernation.

`startServer(token, xsessionid, server_id)` - Start a server when not in hibernation.

`shutdownServer(token, xsessionid, server_id)` - Shutdown a server.

`immediatelyStopServer(token, xsessionid, server_id)` - Force stop a server.

`repairServerFiles(token, xsessionid, server_id)` - Repair your servers files.

`resetServer(token, xsessionid, server_id)` - Reset your server.

`sendCommandToServer(token, xsessionid, server_id, command)` - Send a command to your server.

`changeServerName(token, xsessionid, server_id, new_name)` - Change a server's name. 