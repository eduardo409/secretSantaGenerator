import random
import copy
from time import sleep


#dictionary of name and phone read from file 
def phonebook():
    file = open("data.txt")
    mapOfNames = {}
    for line in file:
        name, phone = line.split(" ")
        mapOfNames[name] = int(phone)
    return(mapOfNames)

def shuffle(listOfNames):
    names = copy.deepcopy(listOfNames)
    random.shuffle(names)
    return names

def generatePairs(listOfNames):
    print("matching ..")
    pairs = matchPairs(listOfNames)
    while(isInvalidMatch(pairs)):
        pairs = matchPairs(listOfNames)
        print("...")
    print("DONE!")
    return pairs
def matchPairs(listOfNames):
    listOfshuffledNames = shuffle(listOfNames)
    pairs = list(zip(listOfNames, listOfshuffledNames))
    return pairs
def printPairs(pairs):
    for name1, name2 in pairs:
        print(name1, "----", name2)
def isInvalidMatch(listOfNames):
    for name1, name2 in listOfNames:
        if(name1 == name2):
            return True
    return False
    
contacts = phonebook() 
def pairs():
    listOfNames = list(contacts.keys())
    pairs = generatePairs(listOfNames)
    return pairs
