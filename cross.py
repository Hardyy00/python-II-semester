a,b,c = input("").split()
a,b,c = int(a),int(b),int(c)

if a==b and b==c and c==a :
    a,b,c = 0,0,0
elif a==b :
    a,b = 0,0
elif a==c :
    a,c = 0,0
elif b==c :
    b,c = 0,0


print(a+b+c)