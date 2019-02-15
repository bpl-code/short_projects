# matchingNumbers.py
# This program randomly creates two lists, then makes a third with only the numbers that exist in both lists 
from random import randint

def main():
    print("This program randomly creates two lists of ints. It then compares them adding any number")
    print("that is in both lists into a third list without adding any duplicates.")
    if input("Press enter to try or 'q' to quit.") != 'q':
        firstList = createList()
        secondList = createList()
        print("{} this is the first list.".format(firstList))
        print("{} this is the second list.".format(secondList))
        thirdList = compareList(firstList, secondList)
        if len(thirdList) == 0:
            print("There were no matching numbers!")
        else:
            print("{} here is the final list of numbers!".format(thirdList))
    else:
        print("Goodbye!")


def createList():
    outputList = []
    for i in range(randint(1,11)):
        outputList.append(randint(1,11))
    return outputList

def compareList(first, second):
    third = []
    for i in range(len(first)):
        if second.count(first[i]) and  not third.count(first[i]):
            third.append(first[i]) 
    return third

main()