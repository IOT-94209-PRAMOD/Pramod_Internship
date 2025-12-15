def count_vowels (str):
    count = 0
    vowels = "aeiouAEIOU"
    for char in str:
        if char in vowels:
            count +=1
    return count

def count_consonant (str):
    count = 0
    vowels = "aeiouAEIOU"
    for char in str:
        if char.isalpha() and char not in vowels:
            count +=1
    return count 
        
def ratio_vowel_consonant (vowels, consonant):
    if consonant == 0:
        return "consonat count is zero, ratio undefined"
    return vowels / consonant
  
        

str = input("enter a string :")

v = count_vowels (str)
c =count_consonant (str)
r = ratio_vowel_consonant (v, c) 

print("number of vowels in the string :",v)
print("number of consonants in the string :",c)     
print("ratio of vowels to consonants in the string :",r)