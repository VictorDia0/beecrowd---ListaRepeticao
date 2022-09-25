par = 0
impar = 0
posi = 0
nega = 0
for a in range(1,6):
    x = int(input())
    if (x % 2) == 0:
        par = par + 1
    if (x % 2) != 0 :
        impar = impar + 1
    if x > 0 :
        posi = posi + 1
    if x < 0 :
        nega = nega + 1
print(f'{par} valor(es) par(es)')
print(f'{impar} valor(es) impar(es)')
print(f'{posi} valor(es) positivo(s)')
print(f'{nega} valor(es) negativoss(s)')
