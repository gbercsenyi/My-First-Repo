def add(num1, num2):
    """Return num1 plis num2 Ez csak egy basic comment"""
    return num1 + num2

def sub(num1, num2):
    """Returns the substart of 2 numbers."""
    return num1 - num2

def mul(num1, num2):
    """Returns multiply of num1 and num2"""
    return num1 * num2

def div(num1, num2):
    """Returns devide of num1 by num2"""
    return num1 / num2

def main():
    doExit = True
    while doExit:
        validInput = False
        while not validInput:
            try:
                num1 = int(input("What is Number1? "))
                num2 = int(input("What us Number2? "))
                operation = int(input("What do you want to do? (1) add, 2) subtract, 3) multiply, 4) divide) Enter a number 1-4: "))
                validInput = True
            except:
                print("Invalid input. Try again...")
                """return  # Exit the program"""
        if operation == 1:
            print("Adding...")
            print(add(num1, num2))
        elif operation == 2:
            print("Subtracking...")
            print(sub(num1, num2))
        elif operation == 3:
            print("Multiplying...")
            print(mul(num1, num2))
        elif operation == 4:
            print("Dividing...")
            print(div(num1, num2))
        else:
            print("I do not understand!")

        exitOrNot = input("Would you like to exit, really??? y/n: ")
        if exitOrNot == "y":
            doExit = False
        elif exitOrNot == "n":
            doExit = True
        else:
            print("I do not understand program will exit now!")
            doExit = False
main()