s = input("\nEnter a string : ")
print("\nElements with even indices :")
for i in range(len(s)) :
    if i%2 == 0 :
        print(s[i])