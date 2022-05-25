r = int(input("\nEnter the number of rows : "))
for i in range(r) :
    for space in range(r-(i+1)) :
        print(" ",end=' ')
    for j in range(2*i+1) :
        print("*",end = ' ')
    print("\n")