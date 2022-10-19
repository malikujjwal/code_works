def checkInclusion(s1, s2):
    charS1 = {}
    charS2 = {}
    start = 0

    for i in s1:
        charS1[i] = 1 + charS1.get(i, 0)
    
    for i in range(len(s2)):
        charS2[s2[i]] = 1 + charS2.get(s2[i], 0)

        if i >= len(s1)-1:
            if charS1 == charS2:
                return True
            else:
                if charS2[s2[start]] == 1:
                    charS2.pop(s2[start])
                else:
                    charS2[s2[start]] -= 1
                start += 1

    return False

print(checkInclusion("ab", "eidboaoo"))
                
