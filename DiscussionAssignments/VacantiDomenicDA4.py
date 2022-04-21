#Domenic Vacanti
#DA 4
#Feb 13, 2020

#DA Problem 1:
def getHawkID():
    return ["dvacanti"]

#DA Problem 2:
def problem1(length, width):
    area = length * width
    return "The area of the rectangle is " + str(area) + " square inches."

#DA Problem 3:
def problem2(aList):
    myLength = len(aList)
    a = 0
    if int(myLength)%2 == 0:
        listSum = sum(aList)
        return listSum
    else:
        return [(str(myLength) + ",") * (int(myLength)-1) + str(int(myLength))]

#DA problem 4:
def problem3(aList):
    for i in range(0,len(aList)):
        aList[i] = aList[i]**2
    return aList

#DA Problem 5:
def problem4(myString1, myString2):
    return myString1 + myString2 + myString1