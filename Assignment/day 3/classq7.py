

# classq7.py

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def power(base, exp):
    if exp == 0:
        return 1
    else:
        return base * power(base, exp - 1)
    


# factorial main function
num = int(input("Enter a number: "))
print(f"Factorial of {num} is {factorial(num)}")

# power main function
base = int(input("Enter base number: "))
exp = int(input("Enter exponent: "))    
print(f"{base} raised to the power of {exp} is {power(base, exp)}") 
