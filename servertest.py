import os
from decimal import Decimal

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
    #cityName = cityName.decode()
    print("Client Requested for City " + cityName)
    if cityName == "NoCity":
        return "No City Entered"#.encode('ascii')
    elif os.path.isfile('./reports/'+ cityName):
        readCityFile(cityName)
        return formattedData(cityName)#.encode('ascii')
    else:
        return "Invalid City Name. Please try again."#.encode('ascii')

# Test Code -------------------------------------------------------------------------------------------
serverStartupChecks()
print(searchForCity("Atlanta"))

# Test Print
# for ic in itemCategoryList:
#     print (ic.name + "\t\t\t" + str(ic.totalSales))




















