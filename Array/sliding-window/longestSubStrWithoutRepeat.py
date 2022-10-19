from timeit import repeat


def lengthOfLongestSubstring(s):
    maxSize, repeatChar = 0,0
    charSubStr = {}
    start,end = 0,0
    for i in range(0, len(s)):
        if s[i] in charSubStr:
            charSubStr[s[i]] += 1
            repeatChar += 1
        else:
            charSubStr[s[i]] = 0
        end += 1
        while repeatChar > 0:
            if charSubStr[s[start]] == 0:
                charSubStr.pop(s[start])    
            elif charSubStr[s[start]] == 1:
                charSubStr[s[start]] -= 1
                repeatChar -= 1
            start += 1
        maxSize = max(maxSize, len(charSubStr))
    return maxSize

print(lengthOfLongestSubstring("aabccbb"))
