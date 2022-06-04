def add(a, b):
    print(a + b)


def subract(a, b):
    print(a - b)


def multipy(a, b):
    print(a * b)


def divide(a, b):
    print(a / b)


ch = "y"


while ch == "y" or ch == "Y":
    x = float(input("Enter your first number : "))
    y = float(input("Enter your second number : "))
    print(" --- Operations Menu --- \n 1.For addition\n 2.For subtraction \n 3.For multiplication\n 4.For division\n")
    op = int(input("Enter your choice : "))

    if op == 1:
        add(x, y)
    elif op == 2:
        subract(x, y)
    elif op == 3:
        multipy(x, y)
    elif op == 4:
        divide(x, y)
    else:
        print("Invalid Choice")
    ch = input("Do you want to continue?(Y/y) : ")
