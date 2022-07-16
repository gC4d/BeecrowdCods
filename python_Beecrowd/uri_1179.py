x = 0
y = 0
par = set()
impar = set()
for i in range(0,15):
    n = int(input())
    if n%2 == 0:
        par.add(n)
    if n%2 != 0:
        impar.add(n)
for j in range(15):
    if x == 5:
        x = 0
        if y == 0:
            y = 1
    if y == 0:
        print(f"par[{x}] = {par[0]}")
        if len(par) >= 1:
            par.pop(0)
        else:
            pass
    if y == 1:
        print(f"impar[{x}] = {impar[0]}") 
        if len(impar) >= 1:
            impar.pop(0)
        else:
            pass
        if len(impar) == 0:
            y == 0
    x+=1

