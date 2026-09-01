import secrets

def generatePin(len):
    x = ""
    for i in range(len):
        x += str(secrets.randbelow(10))
    return(x)
def exitquestion():
    stay = input("Exit: Y/n: ").replace(" ", "")
    if stay.lower() == "y":
        print("Exiting")
    elif stay.lower() == "n":
        main()
    else:
        print("Sorry, input: ", stay ," was not understood.")
        exitquestion()

def main():
    length = input("Number of integers in pin: ")
    length = int(length)
    print(generatePin(length))
    exitquestion()

if __name__ == "__main__":
    main()