#rockpapersissors.py
#This program is a two player rock, paper, sissors game!

def main():
    playGame = "play"
    while playGame == "play":
        player1 = playersChoice("player 1")
        player2 = playersChoice("player 2")
        playGame = runGame(player1, player2)


def playersChoice(player):
    hand = input("{}: choose rock, paper or sissors! > ".format(player))
    if hand != "paper" and hand != "sissors" and hand != "rock":
        hand = input("Opps {} is not an option, please choose from 'rock', 'paper' or 'sissors' : ".format(hand))
    
    print("Interesting choice!")
    return hand

def runGame(player1, player2):
    print("rock!")
    print("paper!")
    print("sissors!")
    print("Go!")
    print("Player 1 chose {} while Player 2 chose {}".format(player1,player2))
    print("{}".format(play(player1, player2)))
    return playAgain()


def play(player1, player2):

    if player1 == player2:
        return "the game is a draw"

    if player1 == "rock" and player2 == "sissors":
        return "Player 1 wins"
    elif player1 == "rock" and player2 == "paper":
        return "player 2 wins"

    if player1 == "paper" and player2 == "rock":
        return "Player 1 wins"
    elif player1 == "paper" and player2 == "sissors":
        return "player 2 wins"
    
    if player1 == "sissors" and player2 == "paper":
        return "Player 1 wins"
    elif player1 == "sissors" and player2 == "rock":
        return "Player 2 wins"

def playAgain():
    userResponse = input("Play again?")
    if userResponse == "yes" or userResponse == "y":
        return "play"
    elif userResponse == "no" or userResponse == "q":
        print("Goodbye")
        return "quit"
    else:
        print("Sorry please reply with 'yes' or 'no'")
        return playAgain()

if __name__ == "__main__":
    main()
