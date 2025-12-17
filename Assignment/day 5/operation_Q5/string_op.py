# string operations module

# string reverse
def reverse(s):
    return s[::-1]

#count vowels in a string
def vowels(s):
    count = 0
    vowels_set = "aeiouAEIOU"
    for char in s:
        if char in vowels_set:
            count += 1
    return count