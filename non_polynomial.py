from itertools import combinations
import time

with open('test/test7') as f:
    lines = f.read().splitlines()
    counter = 0
    for line in lines:
        if(counter == 0):
            n, k = line.split(" ")
            lst = [[None,None] for _ in range(0,int(n))]
        else:
            loc, weight = line.split(" ")
            lst[counter-1] = [int(loc), int(weight)]
        counter = counter + 1

start = time.time()
lstWare = [[None,None] for _ in range(0,int(k))]
minimum = 9999999
comb = combinations(range(0,int(n)), int(k))

for c in comb:
    ans = 0
    for i in range(0,int(k)):
        wHouse = lst[c[i]]
        lstWare[i] = wHouse
    for ind in range(0,int(n)):
        factory = lst[ind]
        road=9999999999
        for wareNum in range(0,int(k)):
            ware = lstWare[wareNum]
            if(abs(ware[0]-factory[0])*factory[1]<road):
                road = abs(ware[0]-factory[0])*factory[1]
        ans = ans + road
    if(ans < minimum):
        minimum = ans
        
finish = time.time()
print("Time"+str(finish-start))
print(minimum)              
