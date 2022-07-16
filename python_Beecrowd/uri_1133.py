x = int(input())
y = int(input())

for i in range(min(x,y)+1,max(x,y)):
    if i%5 == 2 or i%5 == 3:
        print(i)