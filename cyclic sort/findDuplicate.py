def findDuplicateNumber(nums):
    i = 0
    while(i < len(nums)):
        j = nums[i] - 1
        if nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1
    
    return nums[-1]

print(findDuplicateNumber([2, 1, 3, 3, 5, 4]))