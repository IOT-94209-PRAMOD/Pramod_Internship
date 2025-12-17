# math.h
import math as m

# pi
pi = m.pi
print("pi =", pi)

# e
#Returns Euler's number
e = m.e
print("e =", e)

# sqrt
sqart = m.sqrt(5)
print("sqrt(5) =", sqart)

#POWER 
power = m.pow(2, 3)
print("2^3 =", power)

# factorial
fact = m.factorial(5)   
print("5! =", fact) 

# log
log = m.log(100, 10)
print("log base 10 of 100 =", log)

# sin
sin = m.sin(m.pi / 2)
print("sin(pi/2) =", sin)

#product
prod = m.prod([1, 2, 3, 4])
print("product of [1, 2, 3, 4] =", prod)

# gcd
gdc = m.gcd(48, 18)
print("gcd(48, 18) =", gdc)

# lcm
lcm = m.lcm(4, 6)   
print("lcm(4, 6) =", lcm)

# degrees
degrees = m.degrees(m.pi / 2)
print("degrees of pi/2 =", degrees)

# radians
radians = m.radians(90) 
print("radians of 90 degrees =", radians)

# fsum
fsum = m.fsum([1, 2, 3, 4])
print("fsum of [1, 2, 3, 4] =", fsum)

# dist
dist = m.dist((1, 2), (4, 6))
print("distance between (1, 2) and (4, 6) =", dist)

# hypot
hypot = m.hypot(3, 4)
print("hypotenuse of sides 3 and 4 =", hypot)

# os module
import os

#gwetcwd
cwd = os.getcwd()
print("Current Working Directory =", cwd)

#listdir
dir_list = os.listdir('.')
print("List of files and directories in current directory =", dir_list) 

# path module
import os.path as p 

# join
joined  = p.join(cwd, 'new_folder')
print("Joined Path =", joined)  

# exists
path_exists = p.exists(joined)
print("Path exists =", path_exists) 

# isfile
is_file = p.isfile(__file__)
print("Is current file a file? =", is_file) 

# isdir
is_dir = p.isdir(cwd)
print("Is current working directory a directory? =", is_dir)    

# abspath
abs_path = p.abspath(__file__)
print("Absolute path of current file =", abs_path)

# basename
base_name = p.basename(__file__)
print("Base name of current file =", base_name)

# dirname
dict_name = p.dirname(__file__)
print("Directory name of current file =", dict_name)