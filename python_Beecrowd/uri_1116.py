n = int(input())
for i in range(n):
    x,y = [float(k) for k in input().split()]
    if y == 0:
        print("divisao impossivel")
    else:
        print(f"{x/y:.1f}")