#string[start : end : step]

s = input("Enter a string: ")

# starting and ending index slicing
start = int(input("Enter starting index: "))
end = int(input("Enter ending index: "))
print("Sliced string:", s[start:end])

#bassic slicing
print("Original string:", s)
print("First 5 characters:", s[0:5])
print("From index 2 to 6:", s[2:7])
print("From index 3 till end:", s[3:])
print("From beginning to index 4:", s[:5])
print("Every 2nd character:", s[::2])
print("Reversed string:", s[::-1])

# negative slicing
print("Last character:", s[-1])
print("Last 4 characters:", s[-4:])
print("From -6 to -2:", s[-6:-2])

# step slicing
print("Every 3rd character from start to index 10:", s[0:11:3])
print("Every 2nd character from index 5 to 15:", s[5:16:2])
print("Every 2nd character in reverse from index 10 to 0:", s[10:0:-2])