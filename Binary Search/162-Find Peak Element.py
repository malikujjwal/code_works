# 162. Find Peak Element
# check if neighbouring numbers are smaller and move to side with increasing neighbour
class Solution(object):
    def findPeakElement(self, nums):
        def binaryPeak(nums, low, high):
            if high < low:
                return -1
            mid = (low + high)//2
            
            if (mid == 0 or nums[mid] > nums[mid-1]) and (mid == len(nums)-1 or nums[mid] > nums[mid+1]):
                return mid
            
            if nums[mid+1] > nums[mid]:
                return binaryPeak(nums, mid+1, high)
            else:
                return binaryPeak(nums, 0, mid-1)
            
        return binaryPeak(nums, 0, len(nums)-1)