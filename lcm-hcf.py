x = int(input("\nEnter first number : "))
y = int(input("Enter Second number : "))
i=1
print(f"\nLowest Common multiplle of {x} and {y}: ",end='')
while True :
    if i % x == 0 and i % y ==0 :
        print(i)
        break
    else :
        i+=1

i=1
while i<=x and i<=y :
    if x%i==0 and y%i==0 :
        gcd = i
    i+=1

print(f"\nGCD of {x} and {y}: ",gcd,"\n")
