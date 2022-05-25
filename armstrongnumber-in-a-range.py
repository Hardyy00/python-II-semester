import math
print("\nArmstrong numbers between 1 to 500 are :")
for i in range(1,501) :
    ic = i
    sum =  0 
    d = int(math.log10(i)) + 1
    while i!=0 :
        num1 = i%10
        i//=10
        sum+= num1**d
    
    i=ic
    if sum == i :
        print(i)