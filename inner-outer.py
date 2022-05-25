outer = [int(i) for i in input().split()]
inner = [int(i) for i in input().split()]
if len(outer) < len(inner) :
    print(False)
else :
    for i in inner :
        if i in outer :
            f = True
        else :
            f = False
            break
    print(f)