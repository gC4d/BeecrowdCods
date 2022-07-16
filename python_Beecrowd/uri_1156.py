s = 0
i = 3
j = 2
k = 0
while k <= 100:
    if k == 1:
        s+= 1 + (i/j)
    else:
        s+= (i/j)
    i+=2
    j+= j
    k+=1
print(f"{float(round(s)):.2f}")