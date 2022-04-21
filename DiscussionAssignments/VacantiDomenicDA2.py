#Domenic Vacanti
#DA 2
#Section A07
#Feb 2, 2020

#DA Problem 1: First is the Classic getHawkID function
def getHawkID():
    return ["dvacanti"]

#DA Problem 2: Takes three numbers and calculates the average to the nearest
# 10ths placee
#start with defining the function
def calculateAverage(p1, p2, p3):
#add the three numbers together
    p4 = p1 + p2 + p3
    p5 = p4 / 3
    return round(p5, 1)
#devide by thd number of objects (3)
#round to the nearest 10ths spot

#DA Problem 3: Does the smae thing as above but puts it into a str
def getAverageString(p1, p2, p3):
    p4 = p1 + p2 + p3
    p5 = p4 / 3
    #same as above, finding the average of the values
    #Injects the value into a string
    return "The average value is " + str(round(p5, 1)) + "."
    #Returns the string with the value of the average

#DA Problem 4: Take two numbers and multiply them if the letter is "P" and add
#if the letter is "S"
def doMath(p1, p2, myString):
   if myString == "S":
       #if the string is an S it will run the addition function below
       p3 = p1 + p2
       return p3
   elif myString == "P":
       #if the string is a P then it will multiply the p1 and p2
       p3 = p1 * p2
       return p3
   
    
        
    
        