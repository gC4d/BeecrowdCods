a,b,c = [float(x) for x in input().split()]

if (b + c) > a and (a + c) > b and (a + b) > c:
    print(f"Perimetro = {a+b+c:.1f}")
else:
    print(f"Area = {((a+b)* c)/2:.1f}")