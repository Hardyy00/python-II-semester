s = input("\nEnter a string : ")
items = []
print("\n")
for i in s :
    if i in items :
        pass
    else :
        print(f"Frequency of {i} : {s.count(i)}")
        items.append(i)
