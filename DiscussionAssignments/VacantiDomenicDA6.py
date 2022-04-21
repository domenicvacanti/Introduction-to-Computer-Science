#Domenic Vacanti
#DA 6
#A07
#March 5, 2020

def getHawkID():
    return ["dvacanti"]

def returnLetters(myString):
    myList = []
    for i in range(0,len(myString)):
        if myString[i].isalpha() == True:
            myList.append(myString[i])
        else:
            myList
    return myList

def returnUniqueLetters(myString):
    lastList = returnLetters(myString)
    newList = []
    for element in lastList:
        if element in newList:
            newList #:D
        else:
            newList.append(element)
    return newList

def makeTwoListsOfLists(string1,string2):
    lastList = returnLetters(string1)
    lastList1 = returnLetters(string2)
    newList = [lastList] + [lastList1]
    return newList
    
    
