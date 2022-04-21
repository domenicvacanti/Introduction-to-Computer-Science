#Domenic Vacanti
#DA 5
#Section A07
#Feb 27, 20

def getHawkID():
    return ["dvacanti"]

def getSumOdds(aList):
    newTot = 0
    for i in range(0,len(aList),1):
        if i % 2 == 1:
            newTot = newTot + int(aList[i])
    return newTot

def reverseList(myList):
    for i in range(len(myList)-1,-1,-1):
        myList[i] = abs(myList[i])
    myList.sort(reverse=True)
    return myList

def getLetters(myString):
    counter = 0
    myList = []
    for element in myString:
        if element.isalpha() == True:
            if element in myList:
                myList
            else:
                myList.append(element)
    return myList
            
            