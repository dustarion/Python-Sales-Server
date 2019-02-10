import socket
import datetime

def printWelcomeMessage():
    print ("\nWelcome to City Summary Client")

def printInstructions():
    print ("Instructions:")
    print ("send 'q' at any time to quit")
    print ("send 'x' at any time to quit and also stop the server")

def printCurrentTimeStamp():
    print(datetime.datetime.now().ctime())

def getnewsocket():
    return socket.socket(socket.AF_INET, socket.SOCK_STREAM)

exitNow = False

# Program Runtime Code
printCurrentTimeStamp()
print("\n")
printWelcomeMessage()

# Setup the Connection
clientsocket = getnewsocket()
host = "localhost"
try:
    clientsocket.connect((host, 8089))
except ConnectionRefusedError:
    print('Unable to establish a connection with the server.')
    exitNow = True
except:
    exitNow = True
    print('An error occurred.')
# Catch ConnectionRefusedError: [Errno 61] Connection refused

if not exitNow:
    # Print Instructions for User
    printInstructions()

    # Server Code
    while True:
        msg = input("Enter a City Name: ")
        printCurrentTimeStamp()
        print("\n") 
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
            ibuf = clientsocket.recv(1500)
            if len(ibuf) > 0:
                print(ibuf.decode())
            else:
                print("Disconnected")
                print("The connection has dropped.")
                break
        print("\n")
        printCurrentTimeStamp()

print("Terminating City Summary Client\n")
print("\n")
printCurrentTimeStamp()