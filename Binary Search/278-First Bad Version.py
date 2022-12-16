class Solution(object):
    def firstBadVersion(self, n):
        left, right = 1, n
        mid = 0 
        while (right >= left):
            mid = (left + right)//2
            
            if isBadVersion(mid):
                if not isBadVersion(mid-1):
                    break
                right = mid - 1
            else:
                left = mid + 1
        
        return mid