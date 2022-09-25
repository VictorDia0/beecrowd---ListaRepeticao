n = int(input())
x =['']

for y in range (0,n) :
    x.append(int(input()))
    
for y in range(1,n + 1):
    if x[y] == 0 :
        print('NULL')
    elif x[y] > 0 :
        if x[y] % 2 == 0:
            print('EVEN POSITIVE')
        else :
            print('ODD POSITIVE')
    elif x[y] < 0 :
        if x[y] % 2 == 0 :
            print('EVEN NEGATIVE')
        else :
            print('ODD NEGATIVE')