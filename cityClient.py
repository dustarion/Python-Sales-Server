print ("City Client Python") #Remove Later

#!/usr/bin/env python3
#source file: simClient.py
import socket
def getnewsocket():
    return socket.socket(socket.AF_INET, socket.SOCK_STREAM)

clientsocket = getnewsocket()
host = "localhost"
clientsocket.connect((host, 8089))

# Display Instructions on Screen
print ("send ['q' to quit; 'x' to quit and stop the server]")

# Server Code
while True:
    msg = input("Enter a City Name: ")    
    obuf = msg.encode() # convert msg string to bytes
    clientsocket.send(obuf)

    # Client wants to disconnect from server
    if (msg == 'q' or msg == 'x'):
        # q disconnects only
        # x disconnects and shuts the server down
        clientsocket.close()
        break

    # Client wants to send a city name
    else:
        ibuf = clientsocket.recv(255)
        if len(ibuf) > 0:
            print(ibuf.decode())
        else:
            print("The connection has dropped")
            break
print("Bye Bye")
