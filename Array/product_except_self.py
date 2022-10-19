def productExceptSelf(nums):
    res = [0] * len(nums)
    prod = 1
    for i in range(0, len(nums)):
        res[i]= prod
        prod = prod * nums[i]

    prod = 1
    for i in range(len(nums) - 1, -1, -1):
        res[i] = res[i] * prod
        prod = prod * nums[i]

    return res

nums = [1,2,3,4]
print(productExceptSelf(nums))