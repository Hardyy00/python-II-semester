small,big,goal = input("").split()
small,big,goal = int(small),int(big),int(goal)

if goal >= big * 5 :
    remainder = goal - (big*5)
else : 
    remainder = goal % 5

if remainder <= small :
    print(True)
else :
    print(False)