def conflictingAppointments(intervals):
    intervals.sort()
    start, end = 0, len(intervals)-1
    while start < end-1:
        if (intervals[start][1] >= intervals[start+1][0]):
            return False
        start+=1
    return True


print(conflictingAppointments( ([[4,5], [2,3], [3,6]])))
#false