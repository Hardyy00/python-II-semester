len = int(input("\nEnter the length : "))
brea = int(input("Enter the breadth : "))

if (len*brea) > (2*(len+brea)) :
    print("\nArea is greater than perimeter")

elif (len*brea) < (2*(len+brea)) :
    print("\nArea is less than perimeter")

else :
    print("\nArea is equal to perimeter")
