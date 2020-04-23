import asyncio
import requests
import valve.source.a2s
import json 
#This is crap but if you wanted a way to check and restart this is a very simple way to do it
async def check():
    SERVER_ADDRESS = ("",27015)
    def queryserver():
            try: 
                with valve.source.a2s.ServerQuerier(SERVER_ADDRESS) as server:
                    info = server.info()
            except valve.source.NoResponseError:
                return False
            else:
                return True

    while True:
        try: 
            with valve.source.a2s.ServerQuerier(SERVER_ADDRESS) as server:
                info = server.info()
        except valve.source.NoResponseError:
            headers = {"Authorization": "Bearer APikeY"}
            r = requests.get("http://PANELADDRESS/api/client/servers/SERVERID/utilization", headers = headers)
            data = r.json()
            if(queryserver() == False):
                await asyncio.sleep(10) 
                print("Server failed request")
                if(queryserver() == False):
                    await asyncio.sleep(10) 
                    print("Server failed request")
                    if(queryserver() == False):
                        await asyncio.sleep(10) 
                        if(data["attributes"]["state"] == "on"):
                            data = { "signal": "kill" }
                            headers = {"Authorization": "Bearer APIKEY"}
                            requests.post("http://PANELADDRESS/api/client/servers/SERVERID/power", data = data, headers = headers)    
                            asyncio.sleep(5)
                            data = { "signal": "start" }
                            headers = {"Authorization": "Bearer APIKEY"}
                            requests.post("http://PANELADDRESS/api/client/servers/SERVERID/power", data = data, headers = headers)     
                            print("Server Frozen")
                            await asyncio.sleep(30)
            await asyncio.sleep(30)

asyncio.run(check())
