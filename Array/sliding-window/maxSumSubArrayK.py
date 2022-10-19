def maxSum(nums, k):
    start,sum =0,0
    currentSum = 0
    for i in range(0, len(nums)):
        currentSum += nums[i]

        if i >= k-1:
            sum = max(currentSum, sum)
            currentSum -= nums[start]
            start += 1
        
    return sum

print(maxSum([2, 3, 4, 1, 5], 2))