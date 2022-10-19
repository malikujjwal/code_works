def characterReplacement(s, k):
    charCount = {}
    start = 0
    maxf, result = 0, 0

    for end in range(len(s)):
        charCount[s[end]] = 1 + charCount.get(s[end], 0)
        maxf=  max(maxf, charCount[s[end]])

        if (end - start + 1 - maxf) > k:
            charCount[s[start]] -= 1
            start += 1

        result = max(end - start + 1,result)

    return result

print(characterReplacement("AABABBA", 1)) 
        