x = 1
y = 2
while x != y :
    t = input().split()
    x,y = t
    x = int(x)
    y = int (y)
    if x > y :
        print('Decrescente')
    elif x == y:
        break
    else:
        print('Crescente')