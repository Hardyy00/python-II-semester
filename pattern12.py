r = int(input("\nEnter the number of rows : "))
upper = r//2 + 1
for i in range(upper) :
    for space in range(upper-(i+1)) :
        print(" ",end=' ')
    for j in range(2*i+1) :
        print("*",end=' ')
    print("\n")

lower = r - upper
for i in range(lower) :
    
    if i==0 :
        for space in range(i+1) :
            print(" ",end='')
        for j in range(2*lower) :
            print("*",end=' ')
    else :
        for space in range(i+1) :
            print(" ",end=' ')
        for j in range(2*(lower-(i+1)) + 1) :
            print("*",end=' ')
    print("\n")