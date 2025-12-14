def is_prime(num):
    if num <= 1:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False

    return True
start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))

print("Prime numbers in the given range are:")
for n in range(start, end + 1):
    if is_prime(n):
        print(n, end=" ")
