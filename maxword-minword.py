
s = input("\nEnter a string : ").split()
max = s[0]
min = s[0]
for i in s :
    if len(max) < len(i) :
        max = i
    if len(min) > len(i) :
        min = i

print("\nLargest word =",max)
print("Smallest Word =",min)

