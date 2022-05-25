s = input("\nEnter a string : ")
s1 = ''
for i in s :
    if (ord(i)>=65 and ord(i)<=90) or (ord(i)>=97 and ord(i)<=122) :
         s1+=i

print(s1)