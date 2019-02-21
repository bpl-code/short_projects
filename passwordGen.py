#passwordGen.py
#Password generator

#33 to 126 ascii code
# caps 65 - 90 
# symbols 33 - 47 & 58 - 64 & 91 - 96 & 123 - 126

from random import randint

def main():
    #ask what strength password they want
    #if strong run this function 
    #else run this function 
    print(strongPassword())


def strongPassword():
    password = []
    for i in range(randint(12,20)):
        password.append(chr(randint(33,126)))
    return "".join(password)

if __name__ == "__main__":
    main()