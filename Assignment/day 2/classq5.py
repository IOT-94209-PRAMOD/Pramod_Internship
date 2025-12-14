def print_binary(num):
    if num == 0:
        print(0)
        return
    
    binary = ""
    while num > 0:
        remainder = num % 2
        binary = str(remainder) + binary
        num = num // 2
    
    print("Binary format:", binary)
    
num = int(input("Enter a decimal number: "))
print_binary(num)