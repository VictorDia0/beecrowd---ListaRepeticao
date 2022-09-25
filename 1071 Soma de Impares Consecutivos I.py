x = int(input())
y = int(input())

if x > y :
    maior = x
    menor = y
else:
    maior = y
    menor = x
    
menor = menor + 1
res = 0

while (menor < maior) :
    if (menor % 2) != 0 :
        res = res + menor
    menor = menor + 1
print(res)