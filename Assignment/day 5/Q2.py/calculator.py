# Calculator functions
#addition function
def add(a, b):
    return a + b    

# subtraction function
def sub(a, b):
    return a - b

# multiplication function
def mul(a, b):
    return a * b

# division function
def div(a, b):  
    if b != 0:
        return a / b
    else:
        return "Error! Division by zero."
    
# if __name__ == '__main__':
#     # Test the calculator functions
#     x = 15
#     y = 3
#     print(f"Addition of {x} and {y} = {add(x, y)}")
#     print(f"Subtraction of {x} and {y} = {sub(x, y)}")
#     print(f"Multiplication of {x} and {y} = {mul(x, y)}")
#     print(f"Division of {x} and {y} = {div(x, y)}")