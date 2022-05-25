ra = int(input("Enter the age of ram : "))
sa = int(input("Enter the age of shyam : "))
aa = int(input("Enter the age of ajay : "))

if ra<sa and ra<aa :
    name = "ram"
elif sa<ra and sa<aa :
    name = "shyam"
elif aa<ra and aa < sa :
    name =  "ajay"

print(f"\n{name} is youngest of three")