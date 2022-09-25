n = int(input())
in1 = 0
out = 0
for x in range (0,n) :
    x = int(input())
    if x >= 10 and x <= 20 :
        in1 = in1 + 1
    else :
        out = out + 1
print(f'{in1} in')
print(f'{out} out')