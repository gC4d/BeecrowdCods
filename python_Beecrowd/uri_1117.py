media = 0
i = 0
while True:
    x = float(input())
    if x >= 0 and x <= 10:
        media += x
        i+=1
    else:
        print("nota invalida")
    if i == 2:
        print(f"media = {media/2:.2f}")
        break
    