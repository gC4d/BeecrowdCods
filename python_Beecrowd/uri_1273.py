while True:
    vet = []
    size = []
    tamMax = 0
    n = int(input())
    if n == 0:
        break
    for i in range(n):
        txt = input()
        vet.append(txt)
        size.append(len(txt))
        if len(txt) > tamMax:
            tamMax = len(txt)
    #print(vet)#print(size)#print(tamMax)
    for i in range(n):
        if size[i] < tamMax:
            x = tamMax - size[i]
            newTxt = ""
            for j in range(x):
                newTxt+=" "
            vet[i] = newTxt+vet[i]
        print(f"{vet[i]}")
    print()
