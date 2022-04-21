#Domenic Vacanti
#Programming Assignment 4
#Section A07
#March 1, 20
def getHawkID():
    return ["dvacanti"]

def anagrams(string1,string2):
    #If all the elements in string 1 are in string 2 give True
    for element in string1:
        if element in string2:
            string1
            #Do nothing lol
        else:
            return False
    return True

def runLengthEncoding(myList):
    #Take a list of letters, for every letter that is repeated, return the letter and the number of times it was repeated without being inturruped by another different letter
    counter = 0
    myLength = 0
    aList = []
    # ^^^^^^ Set all this up to be added to in the for loop
    for i in range(0, len(myList), 1):
        # \/ it's going to try to do this
        try:
            if myList[counter] == myList[counter + 1]:
                #^^^^ if they equal we want to move up the list 1 space with counter (not needed I don't think with a for loop) and add 1 to the mylength, keeping track of the number of letters in a row.
                myLength = myLength + 1
                counter = counter + 1
            elif myList[counter] != myList[counter + 1]:
                #^^^^^ once two letter do not equal eachother
                aList.append(myList[counter])
                aList.append(myLength + 1)
                myLength = 0
                counter = counter + 1
        except:
            #^^ when the function fails (at the end of the list) this function will add the last two appendages
            aList.append(myList[counter])
            aList.append(myLength + 1)
            return aList
    return aList

def palindrome(myString):
    newString = myString.replace(" ","")
    oofString = newString.lower()
    if oofString == (oofString[::-1]):
        return True
    else:
        return False
