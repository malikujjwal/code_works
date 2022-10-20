def minWindow(s, t):
    if t == "":
        return t
    
    leftIndex, rightIndex = 0, 0
    result = [0,0]
    resultLen = len(s) + 1
    windowS, strT = {}, {}
    for str in t:
        strT[str] = 1 + strT.get(str, 0)
        
    currentSubLen, requiredSubLen = 0, len(strT)
    
    for str in s:
        windowS[str] = 1 + windowS.get(str, 0)
        
        if str in strT and windowS[str] == strT[str]:
            currentSubLen += 1
        
        while currentSubLen == requiredSubLen:
            windowS[s[leftIndex]] -= 1
            
            if s[leftIndex] in strT and windowS[s[leftIndex]] < strT[s[leftIndex]]:
                currentSubLen -= 1
            
            
            if resultLen > rightIndex - leftIndex + 1:
                resultLen = rightIndex - leftIndex + 1
                result[0] = leftIndex
                result[1] = rightIndex+1
            
            leftIndex += 1
        rightIndex += 1
    
    return s[result[0]:result[1]]

print(minWindow("aa","aa"))