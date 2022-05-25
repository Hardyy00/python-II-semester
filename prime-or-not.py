a = int(input("\nEnter a number : "))
i=2
while i<=a-1 :
    if a%i==0 :
        print("\nIts not a prime number ")
        break
    else :
        i+=1

if i==a :
    print("\nIts a Prime number")