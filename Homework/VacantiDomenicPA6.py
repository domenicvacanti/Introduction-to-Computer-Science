#Domenic Vacanti
#Programing Assignment 6
#April 12, 2020
#A07

#Write a function that takes no arguments, and returns a LIST containing your hawkID.  
#Name this function getHawkID().

def  getHawkID():
    return ["dvacanti"]


#Write a function that takes, as an argument, the name of a file, fileName.  
#Your program should open (and read through) the file specified, and return 
#the maximum value in the file.  Name this function maxValueInFile(fileName).
def maxValueInFile(fileName):
    runningWin = 0
    outputFile = open(fileName, "r")
    for char in outputFile.read():
        if int(char) > int(runningWin):
            runningWin = char
    outputFile.close()
    return runningWin
    
    


#Write a function that takes, as an argument, the name of a file, fileName.  
#Your program should open (and read through) the file specified, and return the 
#sum of the squares of the values in the file.  Name this function sumOfSquares(fileName).

def sumOfSquares(fileName):
    outputFile = open(fileName, "r")
    runningTotal = 0
    for char in outputFile.read():
        mySum = int(char)**2
        runningTotal = runningTotal + mySum
    outputFile.close()
    return runningTotal


#Write a function that takes, as an argument, the name of a file, fileName, and an integer n 
#between -750 and 750 (inclusive).  Your program should verify that n is an integer in the correct range.  
#If it is not, it should return the string “Your integer is out of range.”  If it is in the correct range, 
#your program should open (and read through) the file specified, and return the number of values 
#in the file that are greater than n.  Name this function greaterThanN(fileName, n).

def greaterThanN(fileName, n):
    outputFile = open(fileName, "r")
    counter = 0
    if n < 751 and n > -751:
        for char in outputFile.read():
            if int(char) > n:
                counter += 1
        return counter
    else:
        return "Your integer is out of range."
    

'''

OAM program to write:

Write a OAM program that takes, as an argument, as read from the Input Window, a two-digit positive integer, 
and prints the sum of the two digits in the Output Window.  For example, if the value 37 is in the Input
Window, your program should print 10 to the Output Window.

WRITE YOUR PROGRAM HERE, SO THAT THE TA CAN COPY IT AND PASTE IT INTO THE OAMulator to test it.

'''