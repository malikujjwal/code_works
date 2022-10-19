from msilib import sequence


def longestSequence(nums):
    numSet = set(nums)
        
    if (len(nums) == 0):
        return 0
    sequenceCount = 0
    for i in range(0, len(nums)):
        count = 1
        j = 1
        if (nums[i] - j not in numSet):
            while nums[i] + j in numSet:
                count += 1
                j+=1
        sequenceCount = count if count > sequenceCount else sequenceCount

    return sequenceCount

print(longestSequence([]))