#simple calc in python :)
def addiction(firstConst, secondConst):
    print(firstConst + secondConst)

def subtruction(firstConst, secondConst):
    print(firstConst - secondConst)

def multiplication(firstConst, secondConst):
    print(firstConst * secondConst)

def division(firstConst, secondConst):
    print(firstConst / secondConst)

def operation():
    firstConst = float(input("1st: "))
    action = str(input("Hey, what do you want?: "))
    secondConst = float(input("2nd: "))

    if action == '-':
        subtruction(firstConst,secondConst)
    elif action == '+':
        addiction(firstConst,secondConst)
    elif action == "/":
        division(firstConst,secondConst)
    elif action == "*":
        multiplication(firstConst,secondConst)
    elif action == 'x':
        print("Koniec pracy!")
        exit();
    else:
        print("Wrong sign:")

while True:
    operation()

