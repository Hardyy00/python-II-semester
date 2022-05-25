a = input("\nEnter a word : ")
print("\nReversed word : ",end = '')
for i in range(len(a)) :
    print(a[len(a)-1-i],end='')