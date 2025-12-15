# classq5.py
# This module defines basic arithmetic operations and a function to perform calculations using these operations.
def add(x, y):
    return x + y

def subb(x, y):
    return x - y

def mul(x, y):  
    return x * y

def div(x, y):

    return x / y

def calculate(operand1, operand2, operation):
    return operation(operand1, operand2)


print("Addition:", calculate(10, 5, add))
print("Subtraction:", calculate(10, 5, subb))
print("Multiplication:", calculate(10, 5, mul))
print("Division:", calculate(10, 5, div))
# print("Division with zero:", calculate(10, 0, div))