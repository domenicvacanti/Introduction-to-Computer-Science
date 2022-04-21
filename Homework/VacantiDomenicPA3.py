#Domenic Vacanti
#PA 3
#Feb 16, 2020

#PA Problem 1:
def getHawkID():
    return ["dvacanti"]

#PA Problem 2:
def AmIDigits(aList):
    myLength = len(aList)
    i = 0
    counter = 0
    try:
        for i in range(0,len(aList)):
            aList[i] = int(aList[i])
    except:
        return "The length of the input is " + str(myLength) + "."
    
    for i in range(0, len(aList)):
        aList[i] = str(aList[i])
        
    for i in range(0, len(aList)):
        runningTotal = aList[i] + aList[i]
        i = i + 1
    pass

#PA Problem 3:

def findLetters(myList, myString):
    for c in myString:
        found = False
        for s in myList:
            if c in s:
                found = True
        if not found:
            return False
    return True

def finalFunction(myList, n):
    if n < 0:
        return [myList, [0] * abs(n)]
    elif n == 0:
        return myList[-1]
    else:
        total = 0
        for num in myList:
            total += num
        return total
        