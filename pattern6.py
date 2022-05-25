r = int(input("\nEnter the number of rows : "))
for i in range(r) :
    for j in range(i+1) :
        print(f"{j+1}",end = ' ')
    print("\n")