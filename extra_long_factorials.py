def extraLongFactorials(n):
    # if n == 1:
    #     return 1
    # return n*extraLongFactorials(n-1)
    total = 1
    for i in range(1, n+1):
        total *= i
    return total

print(extraLongFactorials(5))