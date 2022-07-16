vi = 0 
vg = 0 
emp = 0
op = 1
grenais = 0
while True:
    if op == 1:
        grenais +=1 
        i,g = [int(x) for x in input().split()]
        if i > g:
            vi += 1
        elif i < g:
            vg += 1
        else:
            emp += 1
        print("Novo grenal (1-sim 2-nao)")
        op = int(input())
    if op == 2:
        break
print(f"{grenais} grenais")
print(f"Inter:{vi}")
print(f"Gremio:{vg}")
print(f"Empates:{emp}")
if vi > vg:
    print("Inter venceu mais")
else:
    print("Gremio venceu mais")