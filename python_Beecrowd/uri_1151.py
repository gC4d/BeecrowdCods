
n  = int(input())
x = 0
aux = 1
aux2 = 0
if n < 2:
    print(0)
if n >= 2:
    print("0 1", end="")
for i in range(n-2):
    x = aux+aux2
    aux2 = aux
    aux = x
    if i < n-3:
        print(f" {x}",end="")
    if i == n-3:
        print(f" {x}")