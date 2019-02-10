print ("City Server Test Code Python") # Delete Later

import os

#TODO
#   check if reports directory exists on server startup

def readCityFile(cityName):
    
    # The filename of the city file
    filename = "./reports/" + cityName

    # Open and read the file!
    file = open(filename, "r")




def searchForCity(cityName = "NoCity"):
    #cityName = cityName.decode()
    print("Client Requested for City " + cityName)
    if cityName == "NoCity":
        return "No City Entered"#.encode('ascii')
    elif os.path.isfile('./reports/Atlanta'):
        readCityFile(cityName)
        return "Exists"#.encode('ascii')
    else:
        print(os.path.isdir('./reports/Atlanta'))
        return "Invalid City Name. Please try again."#.encode('ascii')



#Test code lmaooo
print(searchForCity("Atlanta"))