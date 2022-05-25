popu = 100000

for i in range(1,11) :
    popu = popu - (10/100)*popu
    print(f"\nPopulation {i} years ago = {int(popu)}")