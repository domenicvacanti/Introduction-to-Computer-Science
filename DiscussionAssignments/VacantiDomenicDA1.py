#Domenic Vacanti
#Discussion Assignment 1
#Section A07
#Jan 26, 2020

# DA problem 1 is the one she had us do in class multiple times, the getHawkID
def getHawkID():
    return ["dvacanti"]
#This function will search a list to return my str for grading purposes

# DA Problem 2 is subtracting 2 numbers from eachother
def subtractThem(a,b):
    #This should make subResult equal to a - b
    subResult = a - b
    #Then return the subResult value
    return subResult

# DA Problem 3 adds three numbers into themselves
def addEm(a,b,c):
    addResult = a + b + c
    #This line adds the three numbers together and names the output addResult
    return addResult

# DA Problem 4 echos a str x amount of times
def echo(word, x):
    echoResult = word * x
    #This will multiply the word by the value of x placed in the function
    return echoResult

# DA Problem 5 combines 3 of one word and 3 of another word
def addWords(word1, word2):
    word1Result = word1 * 3
    #This line multiplies the first word by 3
    word2Result = word2 * 3
    #Multiply the second word by 3
    wordResult = word1Result + word2Result
    #This line adds the two results of the multiplication together as
    #wordResult
    return wordResult

# DA Problem 6 takes two numbers and describes the sum of the numbers
def sumDescription(value1, value2):
    value1 = str(value1)
    value2 = str(value2)
    #First we make value 1 and 2 into str so we can print in the return with
    #the strings of text
    value1 = int(value1)
    value2 = int(value2)
    #Then we also set them as int for the equation into the sum
    valueResult = int(value1) + int(value2)
    #We add the ints together to create the value
    valueResult = str(valueResult)
    #Then we turn the sum value into a str to be printed with the return
    return "The sum of " + str(value1) + " and " + str(value2) + " is " + str(valueResult) + "."

# DA Problem 7 takes two words and injects them into a sentence
def introduction(name, town):
    names = str(name)
    towns = str(town)
    #These last two lines turns the name and town into str, makes injection
    #into the sentence avalible
    return "Hello. My name is " + names + ". I love the weather in " + towns + "."
