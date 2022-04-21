#Domenic Vacanti
#DA3
#SECTION A07
#Feb 6, 2020

#DA3: Problem 1
def getHawkID():
    return ["dvacanti"]

#DA3: Problem 2
#Make a function that turns the temp in C to F
def celsiusToFahrenheit(temperature):
    temperatureNew = ((9 * int(temperature))/5) + 32
    return round(temperatureNew)

def celsiusToFahrenheitWords(temperature):
    if 1000 > temperature > (-273.15): 
        newTemp = ((9 * int(temperature))/5) + 32
        return "Notice: " + str(temperature) + " degrees Celsius is equivalent to " + str(round(newTemp)) + " degrees Fahrenheit."
    elif temperature < (-273.15):
        return "Temperature is out of range."
    elif temperature > 1000:
        return "Temperature is out of range."

def AmIBinary(aString):
    n = len(aString)
    if aString.isalpha():
        return "The length of the input is " + str(n) + "."
    elif aString.isdigit():
        for element in aString:
            if element == "0" or element == "1":
                return aString + " is a binary string."
            elif element :
                return "The length of the input is " + str(n) + "."
    pass
            
        
    
       
    
 
     
     