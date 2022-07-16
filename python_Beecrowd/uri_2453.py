
text = input()
text_vet = list(text)
count = 0
n = len(text_vet)
for i in range(n):
    if i == len(text_vet):
        break
    if text_vet[i] == ' ':
        count-=1
    if count % 2 == 0:
        text_vet.pop(i)
       

        count = 1
    count+=1
new_vet = "".join(text_vet)
new_text = str(new_vet).strip('[]')

print(new_text)