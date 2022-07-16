media = 0
i = 0
op = 0
while True:
    x = float(input())
    if x >= 0 and x <= 10:
        media += x
        i+=1
    else:
        print("nota invalida")
    if i == 2:
        print(f"media = {media/2:.2f}")
        if op != 1 or op != 2:
            while True:
                print("novo calculo (1-sim 2-nao)")
                op = int(input())
                if op == 1 or op == 2:
                    break
        if op == 1:
            i = 0
            media = 0
        if op == 2:
            break
        
    