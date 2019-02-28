#passwordGen.py
#Password generator

from random import randint

def main():
    run = True
    while run == True:
        if input("Do you require a strong or weak password?: ") == "strong":
            print(createStrongPassword())
        else:
            print(createWeakPassword())
        if input("Create another password? : Enter 'y' for yes ") != 'y':
            run = False


def createWeakPassword():
    words = ["cat","dog","house","coffee","small","huge","train","world","digital","monk","sky"]
    charLimits = [(48,57),(48,57),(48,57),(33,47)]
    password = []
    capitalWord = words[randint(0,len(words)-1)]
    randomWord = words[randint(0,len(words)-1)]
    password.append(capitalWord.capitalize())
    password.append(randomWord)

    for i in charLimits:
        character = getCharacter(i)
        password.append(character)
    
    password = "".join(password)
    return password


def createStrongPassword():
    password = []
    neededCharacters = [1,2,3,4,4,4,4,4,4,4,4,4] 
    charLimits = {1:(65,90), 2:(33,47), 3:(48,57), 4:(33,126)}
    for i in range(len(neededCharacters)):
        functionCall = neededCharacters.pop(randint(0,len(neededCharacters)-1))
        functionCode = charLimits[functionCall]
        password.append(getCharacter(functionCode))
    password = "".join(password)
    return password


def getCharacter(charType):
    lowerLimit, upperLimit = charType 
    character = chr(randint(lowerLimit, upperLimit))
    return character
    

if __name__ == "__main__":
    main()