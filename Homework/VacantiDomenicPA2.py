#Domenic Vacanti
#PA 2
#Feb 9, 2020

#PA Problem 1
def getHawkID():
    return ["dvacanti"]

#PA Problem 2
def compareToFifty(value1, value2):
    if type(value1) == int and type(value2) == str:
        try:
            myAv = (int(value1) + int(value2))/2
        except:
            return "Invalid Input"
    elif type(value1) == str and type(value2) == int:
        try:
                myAv = (int(value1) + int(value2))/2
        except:
                return "Invalid Input"
    elif type(value1) == str and type(value2) == str:
        try:
                myAv = (int(value1) + int(value2))/2
        except:
                return "Invalid Input"        
    elif type(value1) == int and type(value2) == int:
        myAv = (value1 + value2)/2
    else:
        return "Invalid Input"
    if myAv > 50:
        return "Above 50"
    elif myAv < 50:
        return "Below 50"
    elif myAv == 50:
        return "Equal to 50"
    else:
        return "Invalid Input"
    
#PA Problem 3
def whatAmI(thing):
    counter = 0
    if type(thing) == int:
        return "Integer"
    elif type(thing) == str:
        if thing.isdigit():
            return "String with digits"
        elif thing.isalpha():
            return "String with letters"  
    elif type(thing) == float:
        return "Unidentified object"
    pass
