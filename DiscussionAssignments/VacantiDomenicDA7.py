#Domenic Vacanti
#DA7
#Section A07
#March 15, 2020

def getHawkID():
    return ["dvacanti"]

def problem1(n):
    counter = 1
    myValue = 0
    while counter < n + 1:
        myNew = counter * counter
        myValue = myValue + myNew
        counter = counter + 1
    return myValue

def problem2(slope,intercept,x):
    y = (slope * x) + intercept
    return y

def problem3(aList):
    newList = []
    for i in range(0,len(aList)):
        newList.append(aList[i])
        newList.append(aList[i])
    return newList
def problem4(list1,list2):
    myValue1 = 1
    myValue2 = 1
    for element in list1:
        myValue1 = myValue1 * element
    for element in list2:
        myValue2 = myValue2 * element
    if myValue1 > myValue2:
        return list1
    else:
        return list2