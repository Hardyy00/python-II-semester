r = int(input("\nEnter number of rows : "))
for i in range(r) :
    for space in range(i) :
        print(" ",end=' ')
    for j in range(r-i) :
        print("*",end = ' ')
    print("\n")