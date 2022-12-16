class Solution(object):
    def mySqrt(self, x):
        if x == 0:
            return x
        low, high = 0, x
        
        while high > low:
            mid = (high + low)//2
            
            if (mid*mid) == x:
                return mid
            
            elif mid*mid > x:
                high = mid-1
            elif mid*mid < x:
                break
                
        while (mid*mid)<=x:
            if mid*mid == x:
                return mid
            
            mid = mid+1
        
        return mid-1