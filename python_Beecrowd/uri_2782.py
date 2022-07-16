n = int(input())
n_escadinhas = input(':')
x_ = n_escadinhas.replace(' ', '')
int(x_)
escadinhas = list(x_)

print(escadinhas)

num_escadinhas = 0
dif_escadinhas = 0

if n == 1 or n == 2:
    num_escadinhas+=1

for i in range(n):
    if n > 1:
        dif_escadinhas = escadinhas[i] - escadinhas[i+1]
        if i > 1 and i < n:
            if escadinhas[i] - escadinhas[i+1] != dif_escadinhas :
                num_escadinhas+=1
                dif_escadinhas = 0
        
    
print(num_escadinhas)   