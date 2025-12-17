# main function in Q3.py/main.py

import geometry as g

#for circule area calculation
radius = 5
print(f"area of circule with radius {radius} = {g.circule(radius)}")

# for rectangle area calculation
len = 4
width = 6
print(f"area of rectangle with length {len} and width {width} = {g.rectangle(len, width)}")

if __name__ == '__main__':
    print(f"__name__ = {__name__}")