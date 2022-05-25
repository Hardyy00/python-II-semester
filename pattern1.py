a = int(input("\nEnter the number of rows : "))
for i in range(a//2+1) :
    for j in range(i+1) :
        print("*",end = '')
    print("\n")

for i in range(a-(a//2+1),0,-1) :
    for j in range(i) :
        print("*",end = '')
    print("\n")
