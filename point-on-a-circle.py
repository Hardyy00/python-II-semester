
x,y= input("\nEnter the co-ordinates of the centre of the circle: ").split()
x=int(x);y=int(y)

r = int(input("Enter the radius : "))

x1,y1= input("Enter the co-ordinates of the point : ").split()
x1=int(x1);y1=int(y1)

d = ((x1-x)**2 + (y1-y)**2)**(1/2)

if d == r :
    print("\nPoint lies on the circle")
elif d > r :
    print("\nPoint lies outside the circle")
elif d<r :
    print("\nPoint lies inside the circle")