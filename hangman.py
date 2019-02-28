#hangman.py
#A game of hangman

from random import randint

def main():
    #add a while run
    #start game initialise all needed var
    word,guessLetter,guesses = startGame()
    play = True
    guessesLeft = 10
    print(type(guesses))
    while play:
        #displayword
        displayWord(word,guesses)
        #displayguesses
        displayGuessesLeft(guessesLeft)
        #choose letter 
        guessLetter(guesses)
        #minus a go
        guessesLeft -= 1
        #check if won
        isGameWon(word, guesses)
        if isGameWon != "True" and guessesLeft == 0:
            print("You lost the game!")
            play = False
    


    
def startGame():
    word = selectWord()
    guessesLeft = 10
    guesses = []
    return word, guessesLeft, guesses
    

def selectWord(difficulty="easy"):
    easyWords = ["car","pool","house","cat","mouse","japan","world","building","city"]

    if difficulty == "easy":
        return easyWords[randint(0,len(easyWords)-1)]

def displayWord(word, guesses):
    display = []

    for i in word: 
        if guesses.count(i) > 0:
            display.append(i)
        else:
            display.append("_ ")
    
    print(" ".join(display), "You have guessed the following so far: {}".format(" ".join(guesses)))

def displayGuessesLeft(guessesLeft):
    print("You have {} guesses left!".format(guessesLeft))


def guessLetter(guesses):  
    guessing = True  
    while guessing: 
        guess = input("Guess a letter: ")

        if len(guess) > 1 or len(guess) < 1:
            print("That appears not to be a letter! Please guess a single letter: ")
        elif guesses.count(guess) > 0:
            print("You've already chosen '{}' please choose another letter: ".format(guess))
        else:
            guessing = False   
    
    return guesses.append(guess)

def isGameWon(word, guesses):
    for i in word:
        if guesses.count(i) == 0:
            return False
    return True

if __name__ == "__main__":
    main()