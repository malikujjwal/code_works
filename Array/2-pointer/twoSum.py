def twoSum(self, numbers, target):
    start, end = 0, len(numbers)-1
    while start < end:
        sum = numbers[start] + numbers[end] 
        if sum == target:
            return [start+1,end+1]
        elif sum > target:
            end -= 1
        else:
            start += 1

twoSum([2,7,11,15], 9)