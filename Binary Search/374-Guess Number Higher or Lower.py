class Solution(object):
    def guessNumber(self, n):
        if guess(n) == 0:
            return n
        low, high = 0, n
        
        while (high >= low):
            mid = (high+low)//2
            
            if guess(mid) == 0:
                return mid
            elif guess(mid) == -1:
                high = mid-1
            else:
                low = mid+1