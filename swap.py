a = int(input("\nEnter the value of a : "))
b = int(input("Enter the value of b : "))

print("\nBefore swapping : ")
print(f"a = {a}\nb = {b}")

a = a+b
b = a-b
a = a-b

print("\nAfter swapping :")
print(f"a = {a}\nb = {b}")