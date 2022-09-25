inicio = 0
for a in range(1,6):
    x = int(input())
    if (x % 2 ) == 0:
        inicio = inicio + 1
print(f'{inicio} valores pares')