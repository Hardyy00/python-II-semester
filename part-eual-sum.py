l = [int(i) for i in input().split()]
for i in range(len(l)) :
    if sum(l[:i]) == sum(l[i:]) :
        f = True
        break
    else :
        f = False


print(f)