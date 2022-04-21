#COVID-19 Project

'''

For this project, we will be working with data in two separate files.  The first file
is named us-states.csv, and contains the number of CUMULATIVE COVID-19 cases and deaths 
for each day, starting from 1/21/20.  So, the number of events should be increasing
with time.  The data is sorted by date.

The format for this data is 

date,state,fips,cases,deaths

For example, one line in the file looks like:

1/21/20,Washington,53,1,0

All dates read in from a file are in this format: Month/Day/Year where the Month and Day
are 1 or 2-digit numbers, and the year is a 2-digit number (20, in this case).  The date
format in Python has the year represented in 4 digits (2020) so you must transform
the string for the year accordingly.

Notice that each field is separated by a comma, so when you read each line in the file, you
will want to separate the contents of the file by a comma, and also remove the "new line"
character.

This file includes NEW cases and NEW deaths for each state, for each day that an event occurs.
We will want to develop python programs to help us analyze this information.

The second file includes the name of each state (and the District of Columbia), and its estimated
population based on government census data.  the file is named population.csv, and it has the format

state, population

For example, one line in the file looks like:

Alabama,4903185

This file is useful because each state (and DC) is listed once, so it can be used to generate a list
of all of the names of the states...

For all of the functions that include an event type, you should consistently use the strings
'cases' or 'deaths'.

You may not use ANY functions that have not been discussed in class or in the DA/PA handouts.  That
includes list comprehension, sorting, reversal, slicing, readlines, or any other functions that
do not explicitly appear in the handouts or in sample code.  Any functions that you write that deviate
from this policy will receive a score of 0 for that function.  There are no exceptions to this policy.
If you can use fancy python built-in functions, you should be able to write these functions using
just the basic functions.  Functions that you are allowed to use are: split(), strip(), date(), open(), close()
max(), min().
Remember that if your function opens a file, it must also close it.

You must use any helper functions specified in the function description.

'''

from datetime import date

#write the getHawkID() function (2 points)
def getHawkID():
    return ["dvacanti"]

#write a function that takes, as an argument, a string representing a date
#in the format MM/DD/YY and returns a python date corresponding to that
#date.  Name this function getDateFromString(dateString).  (3 points)
def getDateFromString(dateString):
    splitV = dateString.split("/")
    month = int(splitV[0])
    day = int(splitV[1])
    year = int(splitV[2]) + 2000
    
    return date(year, month, day)
    


#write a function that takes, as an argument, three strings representing dates
#a start date, an end date, and a query date, all three of which are in the format
#MM/DD/YY and returns a Boolean True if the query date is BETWEEN the start and end dates,
#and False if not.  Name this function isInRange(startDate, endDate, queryDate).  (5 points)

def isInRange(startDate, endDate, queryDate):
    startD = getDateFromString(startDate)
    endD = getDateFromString(endDate)
    qD = getDateFromString(queryDate)
    
    if qD > startD and qD < endD:
        return True
    else:
        return False


#write a function that takes, as arguments, a file name, a state, and an event
#which is either 'cases' or 'deaths'.  If the event is 'cases', the function should
#return the STRING in the file that represents the date of the first case, 
#and if the event is 'deaths', the function should return the STRING in the file
#that represents the date of the first death.  If no event has occurred, return the STRING
#'None'.  We will name this function getFirstEvent(fileName, state, event).  (10 points)

def getFirstEvent(fileName, state, event):
    outputFile = open(fileName, "r")
    x = outputFile.read()
    y = x.split(",")
    for i in range(0, len(y)):
        if y[i] == str(state):
            split34 = (y[i+3]).split("\n")
            deathsNumber = split34[0]
            split12 = (y[i-1]).split("\n")
            dateOf = split12[1]
            if event == "cases":
                if deathsNumber == "0":
                    return dateOf
                else:
                    if int(deathsNumber) > 0:
                        return dateOf
            if event == "deaths":
                if int(deathsNumber) > 0:
                    return dateOf
                
                

#write a function that takes, as arguments, a file name and a state, and returns the number of days between the
#first case for the state and the first death reported.  If either no case or no death has been reported
#the function should return the string 'None'.  Name this function caseToDeath(filename, state).  
#You must use the helper functions getDateFromString(dateString) and getFirstEvent(fileName, state, event) 
#as part of this function. Even if you are unable to write those helper functions, assume that they work
#as intended and make use of them here.  you must NOT re-write the contents of those helper functions
#as part of this function.  (10 points)

def caseToDeath(fileName, state):
    neededNumber = 0
    monthDays = [31,29,31,30,31,30,31,31,30,31,30,31]
    firstCase = getFirstEvent(fileName, state, "cases")
    firstDeath = getFirstEvent(fileName, state, "deaths")
    firstCaseDate = getDateFromString(firstCase)
    firstDeathDate = getDateFromString(firstDeath)
    number1 = firstCaseDate.year * 365 + firstCaseDate.day
    for i in range(0,firstCaseDate.month - 1):
        number1 += monthDays[i]
    number2 = firstDeathDate.year * 365 + firstDeathDate.day
    for i in range(0,firstDeathDate.month - 1):
        number2 += monthDays[i]    
    return (number2 - number1)

#write a function that takes, as arguments, the name of the file containing case/death
#data and the name of a file containing population data, and returns the state whose
#time between the first case and the first death is a MAXIMUM value. Hint: use the
#population.csv file to get the name of each state...as you read through that file,
#get the name of each state and use the caseToDeath(fileName, state) helper function to get the number of days
#between the first case and the first death for that state.  keep track of this date
#as well as the corresponding state as you determine the largest of these dates
#your function should return a string containing the name of the state and the number of
#days between the first case and the first death.  For example, if the state were Washington
#and the number of days was 55, your function should return the string 'Washington: 55 days'
#make sure the grammar is correct: if it is 1 day, make sure day is singular.
#name this function maxDaysCaseDeath(caseFile, populationFile).  (10 points)

def maxDaysCaseDeath(caseFile, populationFile):
    outputFile1 = open(populationFile, "r")
    myList = []
    totalDays = 0
    string1 = ""
    popFile = outputFile1.read()
    splitPopFile = popFile.split(",")
    myList.append(splitPopFile[0])
    for i in range(1,len(splitPopFile)-1):
        ssplitPopFile = splitPopFile[i].split("\n")
        myList.append(ssplitPopFile[1])
    for i in range(0,len(myList)):
        runningNumber = caseToDeath(caseFile, myList[i])
        if runningNumber > totalDays:
            totalDays = runningNumber
            string1 = myList[i] 
    if totalDays == 1:
        dayOrDays = "day"
    else:
        dayOrDays = "days"
    return string1 + ": " + str(totalDays) + " " + dayOrDays
        

#write a function that takes, as arguments, the name of the file containing case/death
#data and the name of a file containing population data, and returns the state whose
#time between the first case and the first death is a minimum value. Hint: use the
#population.csv file to get the name of each state...as you read through that file,
#get the name of each state and use the caseToDeath(fileName, state) helper function to get the number of days
#between the first case and the first death for that state.  keep track of this date
#as well as the corresponding state as you determine the smallest of these dates
#your function should return a string containing the name of the state and the number of
#days between the first case and the first death.  For example, if the state were Washington
#and the number of days was 12, your function should return the string 'Washington: 12 days'
#make sure your string is grammatically correct.  if it is 1 day, it should be singular.
#name this function minDaysCaseDeath(caseFile, populationFile).  (10 points)

def minDaysCaseDeath(caseFile, populationFile):
    outputFile1 = open(populationFile, "r")
    myList = []
    totalDays = 100
    string1 = ""
    popFile = outputFile1.read()
    splitPopFile = popFile.split(",")
    myList.append(splitPopFile[0])
    for i in range(1,len(splitPopFile)-1):
        ssplitPopFile = splitPopFile[i].split("\n")
        myList.append(ssplitPopFile[1])
    for i in range(0,len(myList)):
        runningNumber = caseToDeath(caseFile, myList[i])
        if runningNumber < totalDays:
            totalDays = runningNumber
            string1 = myList[i] 
    if totalDays == 1:
        dayOrDays = "day"
    else:
        dayOrDays = "days"
    return string1 + ": " + str(totalDays) + " " + dayOrDays    

#write a function that takes, as arguments, the name of the file containing case/death
#data, a state, a date and an event type.  if the event is 'cases' your function should
#return the number of cases reported on that date, and if the event is 'deaths' your
#function should return the number of deaths on that date.  Name this function
#eventsOnDate(fileName, state, date, event).  (5 points)

def eventsOnDate(fileName, state, date, event):
    outputFile = open(fileName, "r")
    myFile = outputFile.read()
    mySplitFile = myFile.split(",")
    for i in range(0,len(mySplitFile)):
        if state == mySplitFile[i]:
            dateOfEvent = mySplitFile[i-1].split("\n")
            if getDateFromString(date) == getDateFromString(dateOfEvent[1]):
                if event == "cases":
                    return int(mySplitFile[i+2])
                elif event == "deaths":
                    dateOfEventDeath = mySplitFile[i+3].split("\n")
                    return int(dateOfEventDeath[0])
    return 0
                
            
                


#write a function that takes, as an argument, the name of a file that contains case/death data,
#a state, a start date, an end date, and an event type,  if the event is 'cases', your
#function should returns the number of NEW cases between those two dates, and if the
#event type is 'deaths', your function should return the number of NEW deaths between those
#two dates.  You must use the helper function eventsOnDate(fileName, state, date, event)
#that you created previously. Even if you are unable to write that function, you should
#assume that the function exists and that you can use it.  
#Name this function casesBetweenDates(fileName, state, start, end, event).
#(5 points)

def casesBetweenDates(fileName, state, start, end, event):
    outputFile = open(fileName, "r")
    fileSplit = outputFile.read().split(",")
    for i in range(0,len(fileSplit)):
        if fileSplit[i] == state:
            theDate = getDateFromString((fileSplit[i-1].split("\n"))[1])
            startDate = getDateFromString(start)
            endDate = getDateFromString(end)
            deathNumberList = fileSplit[i+3].split("\n")
            if startDate == theDate:
                if event == "cases":
                    startEvent = fileSplit[i+2]
                elif event == "deaths":
                    startEvent = deathNumberList[0]
            if endDate == theDate:
                if event == "cases":
                    endEvent = fileSplit[i+2]
                elif event == "deaths":
                    endEvent = deathNumberList[0]
    number = int(endEvent) - int(startEvent)
    return number
                
    #list of dates plugged into main function to give the event number

#write a program that takes, as arguments, the name of a file containing case/death data,
#the name of a state, and an event, and returns the latest number of events reported.  if the
#event is 'cases' your function should return the highest number of cases reported for that
#state, and if the event is 'deaths' your function should return the highest number of deaths
#reported for that state.  Name this function totalEventsRecorded(fileName, state, event).
#(5 points)

def totalEventsRecorded(fileName, state, event):
    outputFile = open(fileName, "r")
    fileSplit = outputFile.read().split(",")
    runningTotal = 0
    start = "01/01/20"
    end = "01/01/25"
    for i in range(0,len(fileSplit)):
        if fileSplit[i] == state:
            dateList = fileSplit[i-1].split("\n")
            theDate = getDateFromString(dateList[1])
            startDate = getDateFromString(start)
            endDate = getDateFromString(end)
            if theDate > startDate and theDate < endDate:
                if event == "cases":
                    runningTotal = int(fileSplit[i+2])
                elif event == "deaths":
                    theDeaths = fileSplit[i+3].split("\n")
                    runningTotal = int(theDeaths[0])
    return runningTotal


#write a function that takes, as arguments, the name of a file containing case/death data,
#a file containing population data, and an event type, and returns the name of the state
#with the highest number of events in the form of a STRING: 'State: events'  For example,
#if Washington had 45 cases, and it was the highest number of cases of all states, your
#function should return the string 'Washington: 45'  there should be one space between the colon
#and the number of events.  You must use the helper function totalEventsRecorded(fileName, state, event)
#in this function. Name this function mostEvents(caseFile, populationFile, event).
#(5 points)

def mostEvents(caseFile, populationFile, event):
    outputFile1 = open(populationFile, "r")
    myList = []
    myString = ""
    myTotalEvents = 0
    popFile = outputFile1.read()
    splitPopFile = popFile.split(",")
    myList.append(splitPopFile[0])
    for i in range(1,len(splitPopFile)-1):
        ssplitPopFile = splitPopFile[i].split("\n")
        myList.append(ssplitPopFile[1])
    for i in range(0,len(myList)):
        totalEvents = totalEventsRecorded(caseFile, myList[i], event)
        if totalEvents > myTotalEvents:
            myTotalEvents = totalEvents
            myString = myList[i]
    return myString + ": " + str(myTotalEvents)
    

#write a function that takes, as arguments, the name of a file containing case/death data,
#a file containing population data, and an event type (either 'cases' or 'deaths'), 
#and returns total number of events in the US.  Name this function 
#totalUSEvents(caseFile, populationFile, event).  You must use the helper function 
#totalEventsRecorded(caseFile, myState, event) in this function.
#(5 points)

def totalUSEvents(caseFile, populationFile, event):
    outputFile1 = open(populationFile, "r")
    myList = []
    myString = ""
    myTotalEvents = 0
    popFile = outputFile1.read()
    splitPopFile = popFile.split(",")
    myList.append(splitPopFile[0])
    for i in range(1,len(splitPopFile)-1):
        ssplitPopFile = splitPopFile[i].split("\n")
        myList.append(ssplitPopFile[1])
    for i in range(0,len(myList)):
        totalEvents = totalEventsRecorded(caseFile, myList[i], event)
        myTotalEvents += totalEvents
    return myTotalEvents


#write a program that takes, as arguments, the name of a file containing case/death data,
#the name of a state, the population of the state, and an event, and returns the latest 
#number of events per 100,000 people reported.
#if the event is 'cases' your function should return the highest number of cases reported per 100,000 for that
#state, and if the event is 'deaths' your function should return the highest number of deaths per 100,000
#reported for that state.  Your answer should be rounded to a WHOLE NUMBER (no decimal point). 
#You must use the helper function that determines the maximum number of events for the state, 
#totalEventsRecorded(fileName, state, event) in this function.  
#Your answer must be a WHOLE number, not a float...no decimal point!  Name this function 
#eventsPerCapita(fileName, state, population, event).  (5 points)

def eventsPerCapita(fileName, state, population, event):
    outputFile = open(fileName, "r")
    myFile = outputFile.read().split(",")
    eventsR = totalEventsRecorded(fileName, state, event)
    return round((eventsR*100000)/int(population))
    

    
    
#write a function that takes, as arguments, the name of a file containing case/death data,
#a file containing population data, and an event type, and returns the name of the state
#with the highest number of events per 100,000 people in the form of a STRING: 'State: events'  For example,
#if Washington had 45 cases per 100,000, and it was the highest number of cases per 100,000 of all states, your
#function should return the string 'Washington: 45 per 100,000'  there should be one space between the colon
#and the number of events.  You must use the helper function eventsPerCapita(fileName, state, population, event)
#in this function. Name this function mostEventsPerCapita(caseFile, populationFile, event).
#(10 points)

def mostEventsPerCapita(caseFile, populationFile, event):
    outputFile1 = open(populationFile, "r")
    myList = []
    myString = ""
    myList1 = []
    maximum = 0
    popFile = outputFile1.read()
    splitPopFile = popFile.split(",")
    for i in range(1,len(splitPopFile)-1):
        ssplitPopFile = splitPopFile[i].split("\n")
        myList.append(ssplitPopFile[0])
    myList.append(splitPopFile[51])
    myList1.append(splitPopFile[0])
    for i in range(1,len(splitPopFile)-1):
        ssplitPopFile = splitPopFile[i].split("\n")
        myList1.append(ssplitPopFile[1])    
    for i in range(0,len(myList)):
        stateCap = eventsPerCapita(caseFile, myList1[i], myList[i],event)
        if stateCap > maximum:
            maximum = stateCap
            myString = myList1[i]
    return myString + ": " + str(maximum) + " per 100,000"
    


#write a function that takes, as arguments, the name of a file containing case/death data,
#a file containing population data, and an event type, and returns the name of the state
#with the lowest number of events per 100,000 people in the form of a STRING: 'State: events'  For example,
#if Washington had 45 cases per 100,000, and it was the lowest number of cases per 100,000 of all states, your
#function should return the string 'Washington: 45 per 100,000'  there should be one space between the colon
#and the number of events.  You must use the helper function eventsPerCapita(fileName, state, population, event)
#in this function. Name this function fewestEventsPerCapita(caseFile, populationFile, event).
#(10 points)

def fewestEventsPerCapita(caseFile, populationFile, event):
    outputFile1 = open(populationFile, "r")
    myList = []
    myString = ""
    myList1 = []
    popFile = outputFile1.read()
    splitPopFile = popFile.split(",")
    for i in range(1,len(splitPopFile)-1):
        ssplitPopFile = splitPopFile[i].split("\n")
        myList.append(ssplitPopFile[0])
    myList.append(splitPopFile[51])
    myList1.append(splitPopFile[0])
    for i in range(1,len(splitPopFile)-1):
        ssplitPopFile = splitPopFile[i].split("\n")
        myList1.append(ssplitPopFile[1]) 
    minimum = int(myList[0])
    for i in range(0,len(myList)):
        stateCap = eventsPerCapita(caseFile, myList1[i], myList[i],event)
        if stateCap < minimum:
            minimum = stateCap
            myString = myList1[i]
    return myString + ": " + str(minimum) + " per 100,000"