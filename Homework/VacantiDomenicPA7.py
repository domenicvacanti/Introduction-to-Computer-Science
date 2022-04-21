#Write a function that takes no arguments, and returns a LIST containing your hawkID (as a STRING).  
#Name this function getHawkID().  

def getHawkID():
    return ["dvacanti"]


#Write a function that takes, as an argument, a positive integer n, 
#and returns the sum of the digits of the number.  Name this function addDigits(n).
#For example, addDigits(322) should return the value 7.

def addDigits(n):
    runningTotal = 0
    for i in range(0,len(str(n))):
        number = str(n)[i]
        runningTotal = runningTotal + int(number)
    return runningTotal


#Write a function that takes, as an argument, a positive integer n, 
#and returns a LIST consisting of all of the digits of n (as integers) in the same order.  
#Name this function intToList(n).  For example, intToList(123) should return the list [1,2,3].

def intToList(n):
    myList = []
    for i in range(0,len(str(n))):
        myList.append(int(str(n)[i]))
    return myList
        


'''
Write a function that takes, as an argument, either a 16-digit string or positive integer, n, 
and does the following, in this order:
•	Verifies that it consists of only digits (if it fails, return the string “not digits”)
•	Verifies that it consists of 16 digits (if it fails, return the string “wrong length”)
•	If n is a string, it converts n to an integer
•	Creates a list, myList, where each element is a single digit in n, using the function intToList(n) created in Problem 3
•	Multiplies the elements in the even indices of myList by 2, and any products that produce a two-digit number are replaced by the sum of the digits using the function addDigits(n) created in Problem 2 (for example, if an entry at an even index is 8, when multiplied by 2 will equal 16…replace this value with 7 (the sum of the digits)
•	Compute the sum of all of the single digits in myList.  If the sum modulo 10 is equal to 0, the original value, n, is a valid number and should return True.  If the original value, n, is not a valid number, it should return False.  Otherwise, return the string “Invalid entry”.

Name this function checkCreditCard(n).  For example, 

>>>checkCreditCard(4111111111111111) 

should return True, and 

>>>checkCreditCard(4111111111111112) should return False.

'''
def checkCreditCard(n):
    runningTotal = 0
    for i in range(0,len(str(n))):
        if n[i].isalpha() == True:
            return "not digits"
    if len(str(n)) == 16:
        myList = intToList(n)
        for i in range(0,len(str(n))):
            if i % 2 == 0:
                myNumber = myList[i] * 2
                myList[i] = myNumber
        for char in myList:
            runningTotal = runningTotal + char
        if runningTotal % 10 == 0:
            return True
        elif runningTotal % 10 != 0:
            return False
        else:
            return "Invalid entry"
    else:
        return "wrong length"
                    
            

'''
OAM program to write:

Write a OAM program that takes, as an argument, a positive integer, n, as read from the 
Input Window, and prints the following SUM to the Output Window: 2^0 + 2^1 + …+ 2^n.  
For example, if the input value is 3, then your function should print 15 to the output window.
 
 
WRITE YOUR PROGRAM HERE, SO THAT THE TA CAN COPY IT AND PASTE IT INTO THE OAMulator to test it.

'''