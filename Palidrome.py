#Palidrome.py
#A program that checks if the user input is a Palidrome
    
def main():
    print("This program checks whether your chosen word is a palidrome.")   
    userInput = input("Enter a word: ")
    while userInput != 'q':
        print(palidrome(userInput))
        userInput = input("Press 'q' to quit or Enter another word: ")

def palidrome(userInput):
    wordLength = len(userInput)
    wordLengthHalf = int(len(userInput)/2)
    userInput = userInput.lower()
    
    for i in range(wordLengthHalf):
        
        if userInput[i] != userInput[wordLength - 1 - i]:
            return "{} is not a palidrome!".format(userInput)
        
    return "{} is a palidrome!".format(userInput)


if __name__ == "__main__":
    main()