#primeNumber.py
#This program excepts a users number and tells them if it is prime or not

def main():
    run = True
    while run:
        userInput = int(input("Choose a number: "))
        print(primeCheck(userInput))
        if input("Continue? Press y: ") != "y":
            run = False


def primeCheck(userInput):
    primeNumbers = [2,3,5,7,10]

    if primeNumbers.count(userInput) > 0:
        return "{} is a prime number!".format(userInput)

    for i in primeNumbers:
        if i % userInput == 0:
            return "{} is a prime number!".format(userInput)
    return "{} is not a prime number!".format(userInput)


if __name__ == "__main__":
    main()