s = input("\nEnter a string : ")
if len(s)==1 :
    print(s)
else :
    x = s[0]
    y = s[1:-1]
    z = s[-1]
    print(z+y+x)