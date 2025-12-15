# write a program toperform arithmetic operations using functions
def add(x, y):
    return x + y

def subb(x, y):
    return x - y

def mul(x, y):  
    return x * y

def div(x, y):

    return x / y



print("Select operation.")
print("1. Add \n 2. Subtract \n 3. Multiply \n 4. Divide")

a = int(input ("enter firtst number :"))
b = int(input("enter second number :"))
print("enter choice 1/2/3/4 :")
match int(input()):
    case 1:
        print("addition :",add(a, b))
    case 2:
        print("subtraction :",subb(a, b))
    case 3:
        print("multiplaction :", mul(a, b))
    case 4:
        if b != 0:
            print("division :", div(a, b))
        else:
            print("Error: Division by zero is not allowed.")
    case _:
        print("Invalid input")
