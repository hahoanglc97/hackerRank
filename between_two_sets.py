a = [3,4]
b = [24,48]
lcm = []
gcd = []
for i in range(a[-1], b[0] + 1):
    checkL = 1
    for x in a:
        if i % x != 0:
            checkL = 0
    if checkL == 1 and i not in lcm:
        lcm.append(i)
for y in lcm:
    check = 1
    for z in b:
        if z % y != 0:
            check = 0
    if check == 1 and y not in gcd:
        gcd.append(y)

print(len(gcd))
