# 33. Search in Rotated Sorted Array
# check if mid is which sorted half and call the binary search accordingly
class Solution(object):
    def search(self, nums, target):
            
        def binarySearch(nums, low, high, target):
            if low > high:
                return -1
            
            mid = (low + high)//2
            
            if nums[mid] == target:
                return mid
            
            elif (nums[low] <= nums[mid]):
                if nums[mid] >= target and nums[low] <= target: 
                    return binarySearch(nums, low, mid-1, target)
                return binarySearch(nums, mid+1, high, target)
                
            else:
                if nums[mid] <= target and nums[high] >= target:
                    return binarySearch(nums, mid+1, high, target)
                return binarySearch(nums, low, mid-1, target)

        return binarySearch(nums, 0, len(nums)-1, target)