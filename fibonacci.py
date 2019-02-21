#fibonacci.py
#This program asks for a number and gives you the fibonacci sequence

def main():
    userInput = int(input("Enter a number: "))
    sequence,total = fibonacci(userInput)
    print("Sequence: {}".format(sequence))
    print("Total: {}".format(total))

def fibonacci(userInput):
    current = 1
    sequence = [1, current]
    for i in range(userInput):
        current += sequence[len(sequence)-2]
        sequence.append(current)
    return sequence, current

if __name__ == "__main__":
    main()