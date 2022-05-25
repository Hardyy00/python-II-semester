x1,y1 = input("\nEnter the 1st point co-ordinates : ").split()
x2,y2 = input("Enter the 2nd point co-0rdinates : ").split()
x3,y3 = input("Enter the 3rd point co-ordinates : ").split()

x1=int(x1); x2=int(x2); x3=int(x3); y1=int(y1); y2=int(y2); y3=int(y3)

if x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2) == 0 :
    print("\nAll three points fall on straight line.")

else :
    print("\nPoints are non co-linear")