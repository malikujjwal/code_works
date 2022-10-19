def maxArea(height):
    result = 0
    start,end = 0, len(height) - 1

    while start < end:
        result = max(result, min(height[start], height[end]) * (end-start))

        if height[end] > height[start]:
            start += 1
        elif height[start] >= height[end]:
            end -= 1

    return result

print(maxArea([1,1]))