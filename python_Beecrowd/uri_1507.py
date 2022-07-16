n  = int(input())
for i in range(n):
    seq = input()
    q = int(input())
    for j in range(q):
        x = input()
        if x.lower() in seq.lower():
            print("Yes")
        else:
            print("No")