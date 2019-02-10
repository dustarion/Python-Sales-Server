# +---------------------------------------------------------------+
# | City Summary Client                                           |
# +---------------+-----------------------------------------------+
# | Class         | DISM/FT/1A/22                                 |
# +---------------+-----------------------------------------------+
# | Student ID    | P1804317                                      |
# +---------------+-----------------------------------------------+
# | Name          | Ng Wen Jie Dalton Ng                          |
# +---------------+-----------------------------------------------+
# | Assignment    | ST2411 Python Assignment 2                    |
# +---------------+-----------------------------------------------+
# | Date Written  | Sun Feb 10 2019                               |
# +---------------+-----------------------------------------------+

import socket, datetime



def printWelcomeMessage():
    print ("\nWelcome to City Summary Client")

def printInstructions():
    print ("+--------------+")
    print ("| INSTRUCTIONS |")
    print ("+--------------+------------------------------------------------+")
    print ("| Send 'q' at any time to quit.                                 |")
    print ("| Send 'x' at any time to quit and also stop the server.        |")
    print ("+---------------------------------------------------------------+")

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
    # Attempt Connection
    clientsocket.connect((host, 8089))
except ConnectionRefusedError:
    print('Unable to establish a connection with the server.')
    exitNow = True
except:
    exitNow = True
    print('An error occurred.')

# Check if client should terminate
if not exitNow:
    # Should not Terminate
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