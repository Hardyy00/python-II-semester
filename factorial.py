from math import factorial


x = int(input("\nEnter a number : "))

fact =1 
i=1
while i<=x :
    fact *= i
    i+=1

print("\nFactorial of %d : %d"%(x,fact))

