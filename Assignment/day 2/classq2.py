num = int(input("enter five digit number: "))
# rev = reversed(str(num))
if num == int(str(num)[::-1]):
    print("given number is palindrome")

else:
    print("given number is not palindrome")

