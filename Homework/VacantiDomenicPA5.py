#Domenic Vacanti
#PA5
#A07
#March 8, 2020

def getHawkID():
    return ["dvacanti"]

def eightBitStrings(n):
    import random
    myFileName = "eightBits.txt"
    eightBits = open(myFileName,"w")
    for i in range(n):
        myString = ""
        for g in range(8):
            rand = random.randrange(2)
            if rand == 0:
                myString = myString + "0"
            else:
                myString = myString + "1"
        eightBits.write(myString + "\n")
    eightBits.close()
    

def randomCharacters(n,myString):
    import random
    nRandomChar = random.sample(myString, n)
    with open("nRandomCharacters.txt", "w") as file:
        for char in nRandomChar:
            file.write(char + "\n")

def changeTheCase(myFile, case):
    f = open(myFile, "r")
    myFile2 = "upperCase.txt"
    f2 = open(myFile2, "w")
    myFile3 = "lowerCase.txt"
    f3 = open(myFile3, "w")
    for element in f:
        if case == "upper":
            f2.write(element.upper())
        elif case == "lower":
            f3.write(element.lower())
        else:
            return "Invalid parameter."
    if case == "upper":
        return "Converted the file to upper case."
    else:
        return "Converted the file to lower case."