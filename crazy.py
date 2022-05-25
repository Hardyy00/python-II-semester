n = int(input(""))
list = []
for i in range(n) :
    l1 = []
    for j in range(n) :
        l1.append(0)
    list.append(l1)

for i in range(n) :
    a = list[i]
    for j in range(i+1) :
        a[-(j+1)] = j+1
    # list[i] = a

print(list)
        

