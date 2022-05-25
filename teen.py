def teen(n) :
    if n>=13 and n<=19 :
        n=0
    return n
     

a,b,c = input("").split()
a,b,c = int(a),int(b),int(c)

a = teen(a)
b = teen(b)
c = teen(c)

print(a+b+c)
    