s = input("\nEnter a string : ")
l = []
print("\nDuplicate elements :")
for i in s :
    if i in l :
        pass
    else :
        if s.count(i) >=2 :
            print(i,", Frequency :",s.count(i))
        l.append(i)
