n = int(input())
listLed = []
leds = 0
for i in range(n):
    ledStr = input()
    listLed = list(ledStr)
    for j in range(len(listLed)):
        x = int(listLed[j])
        if x == 1:
            leds+=2
        if x == 2 or x == 3 or x == 5:
            leds+=5
        if x == 4:
            leds+=4
        if x == 6 or x == 9 or x == 0:
            leds+=6
        if x == 7:
            leds+=3
        if x == 8:
            leds+=7
    print(f"{leds} leds")
    leds = 0
            