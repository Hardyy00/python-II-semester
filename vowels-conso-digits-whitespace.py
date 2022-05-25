s = input("\nEnter a string : ")
vowels = 0
digits = 0
con = 0
white_space = 0
for i in s :
    if (ord(i)>=65 and ord(i)<=90) or (ord(i)>=97 and ord(i)<=122) :
        if i in ['a','e','i','o','u','A','E','I','O','U'] :
            vowels = vowels + 1
        else :
            con = con + 1
        
    elif i == ' ' :
        white_space = white_space + 1
    elif ord(i)>=48 and ord(i)<=57 :
        digits = digits + 1 


print("Vowels =",vowels)
print("Consonants =",con)
print("Digits =",digits)
print("White Space =",white_space)