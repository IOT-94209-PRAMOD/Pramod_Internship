#calculator module importing in classq2.py 
# import math as m
import calculator as c
# Using functions from calculator module
a = 10
b = 5
print(f"addition of {a} and {b} = {c.add(a, b)}")

print(f"subtracion of {a} and {b} ={c. sub(a, b)}")

print(f"multiplication of {a} and {b} = {c.mul(a, b)}") 

print(f"division of {a} and {b} = {c.div(a, b)}")

if __name__ == '__main__':
    print(f"__name__ in classq2.py = {__name__}")