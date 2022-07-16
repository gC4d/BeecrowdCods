x = [int(l) for l in input().split()]
i = 1
res = 0

while x[i] <= 0:
    if x[i] <=0:
        i = i + 1
    if x[i] > 0:
        break
for c in range(0,x[i]):
    res = res + x[0] + c
   
print(res)