''' 

LAB EXAM 3AB: This exam consists of 3 questions.  Three of the questions relate to writing computer programs in Python
and the fourth question is an OAM question.  Be sure to follow the instructions for this exam, and use the sample input
and output information to test your program.  Your program will be evaluated using different values, so you should
not try to just hard-code the expected answers into your functions!  This file is set up to run without errors.
Make sure that when you submit your final file, it also runs without errors.  Be sure to include the details of 
your getHawkID() function.  

THIS IS LAB EXAM 3AB, MEANING THAT THE MAXIMUM SCORE THAT YOU WILL RECEIVE ON THIS ASSIGNMENT IS 100 POINTS.  THE RUBRIC
FOLLOWS THE SAME RUBRIC AS THE PREVIOUS LAB EXAMS (EXCLUDING THE getHawkID() FUNCTION, OF COURSE!): 

3 PROBLEMS CORRECT EARNS SOME SORT OF A
2 PROBLEMS CORRECT EARNS SOME SORT OF B
1 PROBLEM CORRECT EARNS SOME SORT OF C
0 PROBLEMS CORRECT EARNS SOMETHING IN THE RANGE 0 - 69

'''

#OUR FAMILIAR getHawkID() function:
def getHawkID():
    return ["dvacanti"]


#PROBLEM 1: PYTHON

#Write a function that takes, as arguments, two single-digit integers, n and m, 
#(recall that a digit is a whole number in the interval [0, 9] ), where n > m, and 
#returns the integer consisting of all of the digits in the interval [m, n], in descending order. 
#If n is not greater than m, your function should return the string ‘Invalid Input’ and if 
#either n or m are not within the interval [0, 9] then the function should return the string ‘Out of Range’   

#Name this function problem1(n, m).  For example, >>>problem1(8, 5) 
#should return the integer 8765.  As another example, >>>problem1(2, 2)
#should return the string ‘Invalid Input’.  As a final example, >>>problem1(12, 2)
#should return the string ‘Out of Range’


def problem1(n, m):
    myString = ""
    reverseRange = range(n,m,-1)
    if n > 9 or m > 9:
        return "Out of Range"
    else:
        if n > m:
            for x in reverseRange:
                myString += str(x)
            myString += str(m)
            return int(myString)
        else:
            return "Invalid Input"
            

#PROBLEM 2: PYTHON

#Write a function that takes, as an argument, a string, and returns a string constructed by 
#alternating the characters of the original string together from the front and end of the string, as
#demonstrated in the examples.  Name this function problem2(aString).  For example,
#>>>problem2(“music”) should return the string ‘mcuis’.  As another example, 
#>>>problem2(“television”) should return the string ‘tneoliesvi’.  Notice that in alternating
#characters, start with the first character in the string, then get the last character, then move back to 
#the front of the string, then the back: if the original string is 'ACEFDB' then your function 
#should return the string 'ABCDEF'.
 

def problem2(aString):
    counter = -1
    turnCounter = 0
    missingNum = (((len(aString)-1)//2)+1)
    newString = aString[0]
    while turnCounter < (len(aString)-2):
        newString += aString[counter]
        counter = counter * -1
        turnCounter = turnCounter + 1
        newString += aString[counter]
        counter = (counter + 1) * -1
        turnCounter = turnCounter + 1
    if len(aString) % 2 == 0:
        newString += aString[missingNum]   
    return newString
    
        



#PROBLEM 3: PYTHON
#Write a function that takes two strings as arguments: the first can be any string but 
#the second MUST be a binary string (which you should verify).  

#If the binary string contains an even number of 1s, the function should return the string in reverse order

#If the binary string contains an odd number of 1s, the function should return the string consisting 
#of the first and last letters of the original string; if the string only has one letter, it should 
#return the string with that one letter duplicated.  

#If the second argument is NOT a binary string, the function should return the first string without any modifications.  

#NOTE: You do not have to verify that the inputs are strings; you MUST, however, verify 
#that the second argument is a binary string (but not that it is an integer).  

#Name this function   problem3(myString, binString).  For example, >>>problem3(“hello”, “1100”) 
#should return the string “olleh”.  As another example, >>>problem3(“hello”, “10”)  should return the string “ho”.  
#As a final example, >>>problem3(“hello”, “123”)  should return the string “hello”.

def problem3(myString, binString):
    counter = 0
    counter1 = 1
    newString = ""
    for char in binString:
        if char != "1" and char != "0":
            return myString
    for char in binString:
        if char == "1":
            counter = counter + 1
    if counter % 2 == 0:
        for i in range(0,len(myString)):
            newString += myString[i-(i+counter1)]
            counter1 += 1
    else:
        newString += myString[0]
        newString += myString[-1]
    return newString