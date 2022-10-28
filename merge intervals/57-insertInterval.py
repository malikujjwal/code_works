def insert(intervals, newInterval):
    result = []
    start, end = 0, len(intervals)
    while start < end and intervals[start][1] < newInterval[0]:
        result.append([intervals[start][0], intervals[start][1]])
        start+=1
    while start < end and intervals[start][0] <= newInterval[1]:
        newInterval[0] = min(intervals[start][0], newInterval[0])
        newInterval[1] = max(intervals[start][1], newInterval[1])
        start+=1
    
    result.append(newInterval)
        
    while start < end:
        result.append(intervals[start])    
        start+=1
    
    return result

print(insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]))