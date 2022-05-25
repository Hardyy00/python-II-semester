p = float(input("\nEnter principal amount : "))
r = float(input("Enter Rate of Interest : "))
t = float(input("Enter time : "))

si = (p*r*t)/100
ta = p+si
print(f"Simple interest = {si}\nTotal Amount = {ta}")