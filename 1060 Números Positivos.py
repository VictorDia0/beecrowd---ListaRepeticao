'''inicio = 0
for a in range(1,7):
    x = float(input())
    if x > 0:
        inicio = inicio + 1
print(f'{inicio} valores positivos')'''

quantidade = 0
for i in range(6):
    entrada = float(input())
    if entrada > 0.0:
        quantidade = quantidade + 1

print(quantidade, 'valores positivos')