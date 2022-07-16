while True:
    a,b = [int(x) for x in input().split()]
    if a == 0 and b == 0:
        break
    txt = ""

    for i in range(a,b+1):
        txt+=str(i)
    for i in range(10):
        if i == 0:
            print(f"{txt.count(str(i))}",end="")
        else:
            print(f" {txt.count(str(i))}",end="")
    print()
    
    
    
''' 
cook = {}
for i in range(10):
    cook[str(i)] = 0
for k in range(a,b+1):
    while k != 0:
        i = k % 10
        print(f"i = {i}, k = {k}, k % 10 = {k % 10}")
        cook[str(i)] += 1   
        #print('{} {} {}'.format(k,i,cook[str(i)]))
        k = k // 10
print(' '.join(map(str, cook.values())))
'''