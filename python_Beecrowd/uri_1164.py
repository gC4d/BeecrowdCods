n = int(input())
nuns = 0
for i in range(n):
    x = int(input())
    for j in range(1,x):
        if x%j == 0:
            
            nuns+=j
    
    if nuns == x:
        print(f"{x} eh perfeito")
    else:
        print(f"{x} nao eh perfeito")
    nuns = 0