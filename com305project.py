
import time



def calculate():  
   ans = 0
   for ind in range(0, n):
        factory = lst[ind]
        road = 99999999
        for wareNum in range(0, k):
            ware = lstWare[wareNum]
            if (abs(ware[0] - factory[0])*factory[1]<road):
                road = abs(ware[0] - factory[0])*factory[1]
        ans += road
   print(ans)
   return ans

with open('test7.txt') as f:
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





lstWare = [[None, None]for _ in range(0, int(k))]


start = time.time()
#print(lstWare[0])
minimum = 9999999

k = int(k)
n = int(n)
#placing warehouses to weighted mean
index = 0
for i in range(0, n - k + 1):
    ans = 0
    for idx in range(0, k):
        lstWare[idx][0] = lst[i + idx][0] #factory loc
        lstWare[idx][1] = i + idx #which factory
    for ind in range(0, n):
        factory = lst[ind]
        road = 99999999
        for wareNum in range(0, k):
            ware = lstWare[wareNum]
            if (abs(ware[0] - factory[0])*factory[1]<road):
                road = abs(ware[0] - factory[0])*factory[1]
        ans += road
    print(ans)
    if (ans < minimum):
        index = i
        minimum = ans
for j in range(0, k):
    lstWare[j][1] = index + j
    lstWare[j][0] = lst[index + j][0]


print("It took", time.time()-start, 'seconds.')
print(minimum)

for w in range(0, k):
    print(w + 1, " 'th ware loc: ", lstWare[w][1])

########################################
for w in range(0, k // 2):
    result = 0
   
    while (lstWare[w][1] - 1 >= 0):
        
        lstWare[w][1] -= 1
        lstWare[w][0] = lst[lstWare[w][1]][0]
        ans = 0
        for ind in range(0, n):
            factory = lst[ind]
            road = 99999999
            for wareNum in range(0, k):
                ware = lstWare[wareNum]
                if (abs(ware[0] - factory[0])*factory[1]<road):
                    road = abs(ware[0] - factory[0])*factory[1]
            ans += road
        print(ans)

        if (ans >= minimum):
            lstWare[w][1] += 1
            lstWare[w][0] = lst[lstWare[w][1]][0]
            break
        else:
            print(ans)
            minimum = ans
for w in range(k - 1, k // 2 + 1, -1):
    while (lstWare[w][1] + 1 <= n - 1):
        
        lstWare[w][1] += 1
        lstWare[w][0] = lst[lstWare[w][1]][0]
        ans = 0
        for ind in range(0, n):
            factory = lst[ind]
            road = 99999999
            for wareNum in range(0, k):
                ware = lstWare[wareNum]
                if (abs(ware[0] - factory[0])*factory[1]<road):
                    road = abs(ware[0] - factory[0])*factory[1]
            ans += road
        print(ans)
        if (ans >= minimum):
            lstWare[w][1] -= 1
            lstWare[w][0] = lst[lstWare[w][1]][0]
            break
        else:
            print(ans)
            minimum = ans
print("It took", time.time()-start, 'seconds.')   
print(minimum)

print("Warehouse locations: ")
for i in lstWare:
    print(i[1])
        

         
        
        
    
    
    
