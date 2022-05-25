s = input("\nEnter a string : ")
print('\nString elements on prime indices are : ')
for i in range(len(s)) :
    j=2
    while j<=i-1 :
        if i%j == 0 :
            break
        else :
            j+=1
    if i==j :
        print(s[i])
   