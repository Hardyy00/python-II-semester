year = int(input("\nEnter any year : "))

if (year%4==0 and year%100!=0) or (year%4==0 and year%100==0 and year%400==0):
    print("\nIts a leap year")
else :
    print("\nIts not a leap year")