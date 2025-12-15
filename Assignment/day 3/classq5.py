# classq5.py

def square(n):
    return n * n

def cube(n):
    return n * n * n

def apply(func, value):
    return func(value)

print("Square:", apply(square, 4))
print("Cube:", apply(cube, 4))
