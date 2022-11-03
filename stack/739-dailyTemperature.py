def dailyTemperatures(temperatures):
    # append value to stack if there is no value greater than current
    # while the current temperature is greater than top of stack, pop the top element
    res = [0 for i in range(len(temperatures))]
    stack = []
    
    for i,v in enumerate(temperatures):
        while stack and v > stack[-1][0]:
            value, index = stack.pop()
            res[index] = i - index
        stack.append((v, i))
    return res

print(dailyTemperatures([73,74,75,71,69,72,76,73]))