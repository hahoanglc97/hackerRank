def nonDivisibleSubset(k, s):
    categories = {}
    for i in s:
        key = i % k
        if key in categories.keys():
            item = list(categories[key])
        else:
            item = []
        item.append(i)
        categories.update({key: item})
    keyCat = list(categories.keys())
    for x in range(0, len(keyCat)-1):
        for y in range(x+1, len(keyCat)):
            if keyCat[x] not in categories.keys() or keyCat[y] not in categories.keys():
                continue
            if (keyCat[x] + keyCat[y]) % k == 0:
                if len(categories[keyCat[x]]) > len(categories[keyCat[y]]):
                    del categories[keyCat[y]]
                else:
                    del categories[keyCat[x]]
                    break
    return sum([1 if z[0] == 0 or z[0] * 2 == k else len(z[1]) for z in categories.items()])

def nonDivisibleSubset2(k, s):
    divisibleArray = [i % k for i in s]
    check_arr = []
    for i in set(divisibleArray):
        if k - i not in check_arr and i not in check_arr:
            check_arr.append(i)
    return sum([1 if i == 0 or i * 2 == k else max(divisibleArray.count(i), divisibleArray.count(k-i)) for i in check_arr])



if __name__ == '__main__':
    fptr = open('test_case/non_divisible_subset_test_2.txt', 'r')
    count = 0
    s = []
    n = 0
    k = 0
    result = 0
    while True:
        count += 1

        # Get next line from file
        line = fptr.readline()

        # if line is empty
        # end of file is reached
        if not line:
            break

        if count == 1:
            n, k, result = list(map(int, line.rstrip().split()))
        else:
            contentLine = list(map(int, line.rstrip().split()))
            s.extend(contentLine)

    print('{:15} : {}'.format('Output', nonDivisibleSubset2(k, s)))
    print('{:15} : {}'.format('Expected Output', result))

    fptr.close()
