#Domenic Vacanti
#PA 1
#Section A07
#Feb 2, 2020

#PA Problem 1: Starter, pulls my hawkID for the auto grading
def getHawkID():
    return ["dvacanti"]

#PA Problem 2: Find the midpoints of two sets of values
def getMidpoint(x1, y1, x2, y2):
    #Get the average of the two numbers for both x and y
    x3 = (x1 + x2)/2
    y3 = (y1 + y2)/2
    #put them in a list and round to the nearest tenth spot
    return [round((x3), 1), round((y3), 1)]

#PA Problem 3: Same thing as above but puts it into a string.
def getMidpointString(x1, y1, x2, y2):
    x3 = (x1 + x2)/2
    y3 = (y1 + y2)/2
    #Same thing as above, finding the midpoint of the two points
    #Then I have to inject them into the str while rounding and making my
    #new point set a str as well
    return "The midpoint is the point " + str((round((x3), 1), round((y3), 1))) + "."

#PA Problem 4: Doing the pathagrean therum with the numbers representing
#different parts of the triangle
def getLength(p1, p2, myString):
    myValue1 = p1**2 + p2**2
    myValue2 = p2**2 - p1**2
    #Setting the therum in both with the hyp and the leg
    #first return for the hyp
    if myString == "H":
        return round((myValue1**0.5), 1)
    #Second return for the leg
    elif myString == "S":
        return round((myValue2**0.5), 1)
    