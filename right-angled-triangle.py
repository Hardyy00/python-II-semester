a,b,c = input("\nEnter three sides : ").split()
a,b,c = float(a),float(b),float(c)

if (a**2 == b**2 + c**2) or (b**2 == a**2 + c**2) or\
     (c**2 == a**2 + b**2) :
     print("\nIts a Right Angled Triangle")
else :
    print("\nIts not a Right Angled Triangle")
