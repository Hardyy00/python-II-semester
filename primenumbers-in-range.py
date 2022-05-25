a = int(input("\nEnter starting point : "))
b = int(input("Enter End Point : "))
print(f"Prime Numbers between {a} and {b} are :")
for x in range(a,b+1) :
    i=2
    while i<=x-1 :
        if x%i==0 :
            break
        else :
            i+=1
    if i==x :
        print(x)

