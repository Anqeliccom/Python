import sys
num = int(input())
q = 0

if num == 2 or num == -2: # need to be parsed separately
    q = 1
    print(q)
    sys.exit()

if num % 4 == 0: # for numbers that are powers of two, there is always exactly one unit
        q = 1
        print(q)
        sys.exit()

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


