r = int(input("\nEnter the number of rows : "))
k = 65
for i in range(r) :
    for j in range(i+1) :
        print(f"{chr(k)}",end =' ')
        k+=1
    print("\n")