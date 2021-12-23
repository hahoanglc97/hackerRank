import numpy as np
import math


def formingMagicSquare(s):
    initAllCase = np.array([
        [[8, 1, 6], [3, 5, 7], [4, 9, 2]],
        [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
        [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
        [[2, 9, 4], [7, 5, 3], [6, 1, 8]],
        [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
        [[4, 3, 8], [9, 5, 1], [2, 7, 6]],
        [[6, 7, 2], [1, 5, 9], [8, 3, 4]],
        [[2, 7, 6], [9, 5, 1], [4, 3, 8]]
    ])
    newS = np.array(s)
    lowestCost = 0
    for i in initAllCase:
        costArray = newS - i
        cost = 0
        for x in costArray:
            cost += np.sum(np.absolute(x))
        if lowestCost == 0 or lowestCost > cost:
            lowestCost = cost

    print(lowestCost)


formingMagicSquare([[4, 8, 2], [4, 5, 7], [6, 1, 6]])
