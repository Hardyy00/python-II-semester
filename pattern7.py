r = int(input("\nEnter the number of rows : "))
k=0
for i in range(r) :
    for j in range(i+1) :
        if k==9 :
            k=0
        k+=1
        print(f"{k}",end=' ')
    
    print("\n")