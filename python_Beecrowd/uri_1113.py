while True:
    x,y = [int(x) for x in input().split()]
    if x > y:
        print ("Decrescente")
    if x < y:
        print ("Crescente")
    if x == y:
        break