print("The Menu For Calculator are shown below")

print("1.Addition")
print("2.Substraction")
print("3.Multiplication")
print("4.Division")

num1= int(input("Enter first no: "))
num2= int(input("Enter Second no: "))

choice = int(input("Enter your choice: "))

match  choice :
    case 1:
        sum= num1 + num2
        print("The addition of 2 no is ",sum)
    case 2:
        sum= num1 - num2
        print("The Substraction  of 2 no is ",sum)
    case 3:
        mul = num1 * num2
        print("The multiplication of 2 no is ",mul)
    case 4:
        div = num1 / num2
        print("The Division of 2 no is ",div)
    
