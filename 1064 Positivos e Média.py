a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())

inicio = 0
media = 0

t = [a,b,c,d,e,f]

for a in t :
    if a > 0 :
        inicio = inicio + 1
        media = media + a
print(f'{inicio} valores positivos')
print(f'{media / inicio:.1f}')