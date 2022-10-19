def threeSum(nums):
    result = []
    nums.sort()

    for i,n in enumerate(nums):
        if i > 0 and n== nums[i-1]:
            continue
        start,end = i+1, len(nums) -1
        while start < end:
            sum = n + nums[start] + nums[end]
            if sum == 0:
                result.append([n, nums[start], nums[end]])
                start += 1
                while nums[start] == nums[start-1] and start < end:
                    start += 1
            elif sum > 0:
                end -= 1
            else:
                start += 1
        
    return result

print(threeSum([-1,0,1,2,-1,-4]))