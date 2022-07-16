x = int(input())
z = 0
i = 1
while z <= x:
    z = int(input())
soma = x
while True:
    soma+=x+i
    i+=1
    if soma > z:
        print(i)
        break