n = int(input())

primo = 0
for i in range(n):
    x = int(input())
    for j in range(2,x):
        if x%j == 0:
           # print(f"x%j = {x%j}, x = {x}, j = {j}")
            primo+=1
    if primo == 0:
        print(f"{x} eh primo")
        primo = 0
    if primo != 0:
        print(f"{x} nao eh primo")
        primo = 0
