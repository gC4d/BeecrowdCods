n = int(input())
num = 0
for i in range(n):
    x,y = [int(l) for l in input().split()]
    if x < y:
        for j in range(x+1 ,y):
            if j%2 == 1:
                num+=j
    if x > y:
        for j in range(y+1 ,x):
            if j%2 == 1:
                num+=j
    print(num)
    num = 0
