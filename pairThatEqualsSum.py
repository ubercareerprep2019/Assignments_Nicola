def pairThatEqualsSum(inputArray, targetSum):
    pairsArray = []
    inputArray.sort()
    print(inputArray)
    start = 0
    end = len(inputArray) - 1
    i = 0
    while (start + i) < (end - i):
        val = inputArray[start + i] + inputArray[end - i]
        if val == targetSum:
            pairsArray += [(inputArray[start+i], inputArray[end-i])]
            print(pairsArray)
        elif (abs(val) <= abs(targetSum)):
            start -= 1
        else:
            end += 1
        i += 1
    return pairsArray


print(pairThatEqualsSum([1, 2, 3, 3, 4, 6, 5, 0], 6))
print(pairThatEqualsSum([], 8))
print(pairThatEqualsSum([5, 5, 5, 5], 10))
print(pairThatEqualsSum([-8, -4, -3, -2, -2, 1, 1, 0, 2, 3, 4, 5, 6], -4))
print(pairThatEqualsSum([-1, -7, 8, 4, 2, -2, -6], -8))
