def kdistinctChar(str, k):
    start, distinctChar = 0,0
    arrSize = 0
    subStr = ""
    for i in range(0, len(str)):
        if str[i] not in subStr:
            distinctChar += 1
        subStr += str[i]

        if distinctChar == k:
            arrSize = max(arrSize, len(subStr))
        
        while distinctChar > k:
            subStr = subStr[1:]
            if str[start] not in subStr:
                distinctChar -= 1
            start += 1

    return arrSize


print(kdistinctChar("cbbebi", 3))