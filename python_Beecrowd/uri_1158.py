n = int(input())
l = 0
aux = 0
soma = 0
for i in range(n):
    x,y = [int(k) for k in input().split()]
    aux = x
    while l < y:
        if aux%2 != 0:
            soma+=aux
            l+=1
        aux+=1
    print(soma)
    soma = 0
    l = 0