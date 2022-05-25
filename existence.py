a , b , c = input("\nEnter three sides : ").split()
a = int(a); b = int(b) ; c = int(c)

if a>b and a>c and b+c>a :
    print("\nTriangle exist")
elif b>a and b>c and a+c>b :
    print("\nTriangle exist")
elif c>a and c>b and a+b>c :
    print("\nTriangle exist")
else :
    print("\nTriangle doesn't exist")