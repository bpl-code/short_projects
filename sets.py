#sets.py
#This program creates a new list out of random list of numbers, except it removes all duplicates
from random import randint

def main():
    oldList = createList()
    print("old list {}".format(oldList))
    newlist = createSet(oldList)
    print("New list {}".format(newlist))


def createList(length=10):
    outputList = []
    for i in range(length):
        outputList.append(randint(1,10))
    return outputList

def createSet(oldList):
    finalList = set()
    for i in oldList:
        finalList.add(i)
    return finalList

if __name__ == "__main__":
    main()