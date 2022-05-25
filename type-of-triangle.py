a,b,c = input("\nEnter three sides : ").split()
a=int(a);b=int(b);c=int(c)

if a==b and b==c :
    print("\nIts an equilateral triagle.")
elif (a==b and b!=c) or (a!=b and b==c) or (a==c and c!=b) :
    print("\nIts an Isosceles triangle.")
elif a!=b and b!=c and c!=a :
    print("\nIts an Scalene triangle.")


if (a**2 + b**2 == c**2) or (b**2 + c**2 == a**2) or (a**2 + c**2 == b**2) :
    print("\nRight angled triangle")