import sys
num = int(input())
q = 0

if num < 0:
    num = abs(num)
    firstUnit = False
    while num:
        if num % 2:
            firstUnit = True
        elif firstUnit:
            q += 1
        num = num // 2  
    q += 2  # sign bit and first unit

else:
    while num:
        q += (num % 2)
        num = num // 2

print(q)


