x = int(input())
y = int(input())
res = 0
for i in range(min(y,x), max(x,y)+1):
    if i%13 != 0:
        res+=i
print(res)