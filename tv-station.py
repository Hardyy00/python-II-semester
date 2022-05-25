day = input("\nEnter the Day : ")
station = input("\nEnter the name of the station : ")
l = []
while True :
    print("\nEnter the Name of the Show : ")
    i = input()
    if i == '' :
        break
    else :
        start = input("\nEnter the Starting time : ")
        stop = input("\nEnter the stoping time : ")
        l.append([i,start,stop])

print(f"\nTV schedule for {station.capitalize()} for {day.capitalize()} :\n")
l = [["Program" , 'Starting time', 'Stopping Time']] + l
for i in range(len(l)) :
    for j in range(len(l[i])) :
        print(l[i][j],end = '   ')
    print("\n")


