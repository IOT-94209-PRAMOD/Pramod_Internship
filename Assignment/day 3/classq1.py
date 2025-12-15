s1 = "pramod"
s2 = "garje"

#string concatenation
print(s1 + " " + s2)   

#string repetition
print(s1 * 3)

#string slicing
print(s1[0:3]) 
print(s2[2:5])

#string length
print(len(s1))
print(len(s2))

#string conversion to uppercase
print(s1.upper())   
print(s2.upper())

#string conversion to lowercase
print(s1.lower())
print(s2.lower())   

#string replacement
print(s1.replace("p", "P"))
print(s2.replace("g", "G"))

#string capitalize
print(s1.capitalize())
print(s2.capitalize())

#string find
print(s1.find("m"))
print(s1.find("z"))
print(s2.find("p"))

print(s2.find("r"))

#string split
print(s1.split(" "))

#string strip
s3 = "   hello world   "    
print(s3.strip())
print(s3.lstrip())
print(s3.rstrip())

#string isalpha
print(s1.isalpha())

#string isdigit
s4 = "12345"    
print(s4.isdigit()) 
print(s1.isdigit())

#string join
print(" ".join([s1, s2]))

#striging format    
age = 21
print("My name is {} and I am {} years old.".format(s1, age))

#string count
print(s1.count("o"))

# #string startswith
# print(s2.startswith("g"))

# #string endswith
# print(s2.endswith("e"))

#string index
print(s1.index("r"))

#string replace
print(s3.replace("hello world","hello duniyaa"))

