def trap(height):
    if not height:
        return 0
    
    water = 0
    start, lMax = 0, height[0]
    end, rMax = len(height) - 1, height[len(height) - 1]

    while start < end:
        if rMax > lMax:
            start += 1
            lMax = max(lMax, height[start])
            water += lMax - height[start]
        else:
            end -= 1
            rMax = max(rMax, height[end])
            water += rMax - height[end]    
    return water 

print(trap([5,4,1,2]))