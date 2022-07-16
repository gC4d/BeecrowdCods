vet = []
vet2 = []
vet = input().split()
for i in range(len(vet)):
    vet[i] = int(vet[i])
    vet2.append(vet[i])
vet2.sort()
for i in range(len(vet)):
    x = vet2[i]
    print(x)
print()
for i in range(len(vet)):
    print(vet[i])