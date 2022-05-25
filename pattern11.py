r = int(input("\nEnter number of rows : "))
for i in range(r) :
    for j in range(2*r+3) :
        if i==0 or i==r-1 :
            print("*",end='')
        else :
            if j==0 or j== (2*r + 3)-1 :
                print("*",end='')
            else :
                print(" ",end='')
    print("\n")