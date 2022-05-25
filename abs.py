a,b = input("").split()
a,b = int(a),int(b)

if (a == 6 or b == 6) or (a+b == 6) or (abs(a-b)==6) :
    print(True)
else :
    print(False)