#Palidrome.py
#A program that checks if the user input is a Palidrome

def reverseString(inputString):
    outputString = ""

    for i in range(len(inputString)-1, -1, -1):
        outputString += inputString[i]

    return outputString

def palidrome(userInput):
    wordLength = len(userInput)
    userInput = userInput.lower()

    if userInput[:1] != userInput[wordLength - 1:]:
        return "{} is not a palidrome".format(userInput.capitalize())
    else:
        halfLength = int(wordLength / 2)
        firstHalfOfWord = userInput[:halfLength]

        if wordLength%2 != 0:
            secondHalfOfWord = userInput[halfLength + 1:]
        else:
            secondHalfOfWord = userInput[halfLength:]

        secondHalfReversed = reverseString(secondHalfOfWord)
        
        if firstHalfOfWord == secondHalfReversed:
            return "{} is a palidrome".format(userInput.capitalize())
        else:
            return "{} is not a palidrome".format(userInput.capitalize()) 

print("This program chekcs whether your chosen word is a palidrome.")       
print(palidrome(input("Enter a word: ")))



