x,y = input("\nEnter the coordinates : ").split()
x = int(x) ; y = int(y)

if x==0 and y!=0 :
    print("\nPoint lies on Y-axis")
elif x!=0 and y==0 :
    print("\nPoint lies on X-axis")
elif x==0 and y==0 :
    print('\nPoint lies on the origin')
elif x!=0 and y!=0 :
    print("\nPoint doesn't lie x-axis or y-axis or origin ")