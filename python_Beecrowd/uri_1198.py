z = 0
try:
    while True:
        x,y = [int(k) for k in input().split()]
        z = max(x,y) - min(x,y)
        print(z)
except EOFError:
    pass