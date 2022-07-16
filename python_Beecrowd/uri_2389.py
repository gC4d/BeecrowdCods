n = int(input())

aux = 0
prod = 0
eucalipto = 0
carvalho = 0
y = 2
x = 0

cont = 0
x+=1

prod = (x * y + ((x-1) * (y-1)))

prod = carvalho + eucalipto

if prod == n:
    cont+=1
    
while y < x :
    aux = 0
    x = 1
    while aux > -1:
        x+=1

        prod = (x * y + ((x-1) * (y-1)))

        prod = carvalho + eucalipto

        if prod == n:
            cont+=1
        if prod >= n:
            aux = -1
            continue
    y+=1
    aux = 0
print(cont)
