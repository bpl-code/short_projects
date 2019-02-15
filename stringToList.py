#stringToList.py
#String to list recursive function

def stringToList(userString, stringList):
    stringList.append(userString[:1])
    if len(userString) == 1:
        return stringList
    return stringToList(userString[1:], stringList)
    
print(stringToList(input("Type a string you want converted to a list: "), []))