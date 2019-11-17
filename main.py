import valve.source.a2s
import time

SERVER_ADDRESS = ("ServerIp here",PORT HERE)

starttime=time.time()
with valve.source.a2s.ServerQuerier(SERVER_ADDRESS) as server:
    while True:
        try: 
            server.get_response
        except:
            print("Server Down")
        else:
            print("Server Responded")
        time.sleep(300 - ((time.time() - starttime) % 300.0))

