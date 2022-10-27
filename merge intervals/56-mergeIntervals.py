def merge(intervals):
        if len(intervals) < 2:
            return intervals
        
        intervals.sort()
        
        result = [[intervals[0][0], intervals[0][1]]]
        i,j = 0,1
        while j < len(intervals):
            if result[i][1] >= intervals[j][0]:
                rightDigit = max(result[i][1], intervals[j][1])
                result[i][1] = rightDigit
                j += 1
            else:
                result.append([intervals[j][0], intervals[j][1]])
                i += 1
                j += 1
            
        return result

print(merge([[1,3],[2,6],[8,10],[15,18]]))