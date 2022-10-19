from pickle import FALSE, TRUE


def isDuplicate(nums):
    arrDict = {}     ##use hashsets instead of dict

    for x in nums:
        if(arrDict.get(x) == "True"):
            return True
        else:
            arrDict[x] = "True"

    return False


arr = [1,2,3,4]
print(isDuplicate(arr))