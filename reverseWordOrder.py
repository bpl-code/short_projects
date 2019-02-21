#reverseWordOrder.py
#This program asks for a user string and reverses the word order

def main():
    run = True
    while run:
        userString = input("Type a multi-word string: ")
        userList = splitStringByWord(userString)
        reversedList = reverseListOrder(userList)
        finalString = joinList(reversedList)
        print(finalString)
        if input("Enter another string? Type 'y' to continue: ") != "y":
            run = False


def splitStringByWord(userString):
    splitString = userString.split(" ")
    return splitString


def reverseListOrder(userList):
    reverseList = []
    for i in range(len(userList)-1, -1, -1):
        reverseList.append(userList[i])
    return reverseList

def joinList(reversedList):
    finalString = " ".join(reversedList)
    return finalString


if __name__ == "__main__":
    main()