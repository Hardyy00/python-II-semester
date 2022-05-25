r = int(input("\nEnter number of rows : "))
print("\n")
for i in range(r) :
    for j in range(r-i) :
        print("*",end = " ")
    print("\n")