n = int(input())
dias = 0
for i in range(n):
    x = float(input())
    while x > 1:

        x = x/2
        dias+=1
    print(f"{dias} dias")
    dias = 0