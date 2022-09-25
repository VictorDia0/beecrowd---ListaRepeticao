aux = 0
m = 0
n = 0

cond = True
while cond:
    x, y = map(int, input().split())
    
    if(x <= 0 or y <= 0):
        break
    
    if x > y :
        m = x
        n = y
    elif x < y:
        m = y
        n = x
    
    if m > n :
        aux = m
        m = n
        n = aux
    soma = 0
       
    while m <= n :
        print(m, end=' ')
        soma = soma + m 
        m= m + 1 
    print(f"Sum={soma}")
