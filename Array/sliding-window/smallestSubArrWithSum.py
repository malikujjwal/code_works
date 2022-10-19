def smallestSubArrayForSum(nums, sum):
    start,currentSum = 0,0
    subArrLen = len(nums) +1
    for i in range(0, len(nums)):
        currentSum += nums[i]

        while currentSum >= sum:
           subArrLen = min(subArrLen, i-start+1)
           currentSum -= nums[start]
           start += 1

    return 0 if subArrLen == len(nums)+1 else subArrLen

print(smallestSubArrayForSum([3, 4, 1, 1, 6], 8))