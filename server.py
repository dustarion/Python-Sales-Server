print ("City Server Python") #Remove Later

import socket
import os
from decimal import Decimal


#  ______   _______  _______  _______ 
# |      | |   _   ||       ||   _   |
# |  _    ||  |_|  ||_     _||  |_|  |
# | | |   ||       |  |   |  |       |
# | |_|   ||       |  |   |  |       |
# |       ||   _   |  |   |  |   _   |
# |______| |__| |__|  |___|  |__| |__|

# Data Section

# Classes
class itemCategory:
  def __init__(self, name, totalSales):
    self.name = name
    self.totalSales = totalSales
# ------------------------------------

# Global Variables
itemCategoryList = []
totalSales = 0

# Returns the number of Item Categories
def icCount():
    return len(itemCategoryList)

# Adds a new/existing Item Category into the array itemCategoryList
def addItemCategory(newic):
    if (icCount == 0):
        # List is empty, just add.
        itemCategoryList.append(newic)
    else:
        for ic in itemCategoryList:
            if ic.name == newic.name:
                # The item category already exists, so add-on to the total sales.
                ic.totalSales += newic.totalSales
                return # Return out of the function.

        # No existing item categories.
        # Since it is new, add it.
        itemCategoryList.append(newic)

# Get an array containing the top three and bottom three sorted
def top3Bottom3():
    # Top Three Item Categories
    icRank = []

    # Initialise the Top3 and Bottom 3,
    # Index 0,1,2 are top 3 respectively, where 0 is the largest.
    # Index 3,4,5 are bottom 3 respectively, where 5 is the smallest.
    for x in range(6):
        if x < 3:
            icRank.append(itemCategory("", Decimal('-inf')))
        else:
            icRank.append(itemCategory("", Decimal('inf')))

    for ic in itemCategoryList:

        # Top Three
        if ic.totalSales > icRank[0].totalSales:
            icRank[2] = icRank[1]
            icRank[1] = icRank[0]
            icRank[0] = ic
        elif ic.totalSales > icRank[1].totalSales:
            icRank[2] = icRank[1]
            icRank[1] = ic
        elif ic.totalSales > icRank[2].totalSales:
            icRank[2] = ic

        # Bottom Three
        if ic.totalSales < icRank[5].totalSales:
            icRank[3] = icRank[4]
            icRank[4] = icRank[5]
            icRank[5] = ic
        elif ic.totalSales < icRank[4].totalSales:
            icRank[3] = icRank[4]
            icRank[4] = ic
        elif ic.totalSales < icRank[3].totalSales:
            icRank[3] = ic

    # ------------------------------------
    return icRank

# Use this to turn the data in itemCategoryList into a string that can be sent to the client.
def formattedData(cityName):
    # Append new lines to returnData
    returnData = []

    returnData.append("Total Sales from " + cityName + " is : $" + str(totalSales))
    
    catCount = len(itemCategoryList) # Number of Categories
    avgSales = round((totalSales/catCount), 2)
    returnData.append("The Average Sales From " + str(catCount) + " Item Categories is : $" + str(avgSales))

    # Check if city has less than 3 item categories
    if catCount <= 3:
        # Exit Now
        returnData = '\n'.join((returnData))
        return returnData

    # Check for top 3 and bottom 3 item categories
    icSorted = top3Bottom3()

    returnData.append("\n")

    # Top 3
    returnData.append("Top Three Item Categories\n=================================================================")
    returnData.append('{:50}'.format(icSorted[0].name) + '{:>15}'.format(str(icSorted[0].totalSales)))
    returnData.append('{:50}'.format(icSorted[1].name) + '{:>15}'.format(str(icSorted[1].totalSales)))
    returnData.append('{:50}'.format(icSorted[2].name) + '{:>15}'.format(str(icSorted[2].totalSales)))
    returnData.append("=================================================================")

    # Bottom 3
    returnData.append("Bottom Three Item Categories\n=================================================================")
    returnData.append('{:50}'.format(icSorted[3].name) + '{:>15}'.format(str(icSorted[3].totalSales)))
    returnData.append('{:50}'.format(icSorted[4].name) + '{:>15}'.format(str(icSorted[4].totalSales)))
    returnData.append('{:50}'.format(icSorted[5].name) + '{:>15}'.format(str(icSorted[5].totalSales)))
    returnData.append("=================================================================")

    # Convert into a single string
    returnData = '\n'.join((returnData))
    return returnData

#Top Three Item Categories\n=======================================================================\n


# Processes a line from the city file into an item category.
def processCityLine(line):
    # Make the line into an array of strings based on the seperator \t (TAB)
    line = line.split('\t')

    # Check if Line is Correct Format Here ---------------------------------------------------------

    # Format of a standard entry is as follows:
    # 2012-12-31    17:53   Atlanta Books   456.66  Cash
    name = line[3]
    salesAmt = Decimal(line[4])

    return itemCategory(name, salesAmt)


def readCityFile(cityName):
    
    # The filename of the city file
    filename = "./reports/" + cityName

    # Open and read the file!
    file = open(filename, "r")

    while True:
        line = file.readline()
        if line == "":
            break
        else:
            # print(line)
            ic = processCityLine(line)
            global totalSales # Initialise totalSales so python knows its not local
            totalSales += ic.totalSales # Add to the total sales
            addItemCategory(ic)
    # ----------------------------

    # All done, close the file!
    file.close()

# --------------------------------


def searchForCity(cityName = "NoCity"):
    cityName = cityName.decode()
    print("Client Requested for City " + cityName)
    if cityName == "NoCity":
        return "nocity"
    elif os.path.isfile('./reports/'+ cityName):
        readCityFile(cityName)
        return formattedData(cityName)
    else:
        return "nocity"

#  __    _  _______  _______  _     _  _______  ______    ___   _ 
# |  |  | ||       ||       || | _ | ||       ||    _ |  |   | | |
# |   |_| ||    ___||_     _|| || || ||   _   ||   | ||  |   |_| |
# |       ||   |___   |   |  |       ||  | |  ||   |_||_ |      _|
# |  _    ||    ___|  |   |  |       ||  |_|  ||    __  ||     |_ 
# | | |   ||   |___   |   |  |   _   ||       ||   |  | ||    _  |
# |_|  |__||_______|  |___|  |__| |__||_______||___|  |_||___| |_|

def serverStartupChecks():
    print ("Server Startup Checks")
    print ("Checking Server Environment...")
    # Ensure Reports Folder Exists
    if not (os.path.isdir('./reports/')):
        print ("Reports Folder is Missing")
        print ("Server Failed to Startup")
        return False
    print ("Reports Folder Exists...")

    print ("Checking Done")
    return True

def printWelcomeMessage():
    print("ST2411 Python and C Sales Summary Server")
    print("\n")

# Network Section
def handler(con):
    while True:
        buf = con.recv(1500) # buf is of the type of byte
        if len(buf) > 0:
            print("User sent:")
            print(buf.decode())  # decode with system default encoding scheme
            print("\n")

            if buf == b"q" or buf == b"x":
                break
            else:
                # Search for city, respond to client with approriate data.
                #.encode('ascii')"Invalid City Name. Please try again.".encode('ascii')
                sendData = searchForCity(buf)
                if sendData == "nocity":
                    con.sendall("Invalid City Name. Please try again.".encode('ascii'))
                else:
                    con.sendall(sendData.encode('ascii'))
        else: # 0 length buf implies client has dropped the con.
            return ""  # quit this handler immediately and return ""  
    con.close() #exit from the loop when client sent q or x
    return buf.decode()


# Server Runtime Code
printWelcomeMessage()

# Check Server Environment
if serverStartupChecks():
    # Start Server
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serversocket.bind(('0.0.0.0', 8089))
    serversocket.listen(5) # become a server socket, up to 5 connections

    while True:
        print("\n\nWaiting for a new call at accept()")
        connection, address = serversocket.accept()
        if handler(connection) == 'x':
            break; 
    serversocket.close()

print("Stopping Server\n")















