def validAnagram(s1, s2):
    sort_s1 = ''.join(sorted(s1))
    sort_s2 = ''.join(sorted(s2))
    if (sort_s1 == sort_s2):
        return "TRUE"
    return "FALSE"

def validAnagramDict(s1, s2):
    if (len(s1) != len(s2)):
        return "FALSE"
    
    dictS, dictT = {}, {}

    for x in range(0, len(s1)):
        dictS[s1[x]] = s1[x];
        dictT[s2[x]] = s2[x];
    
    if (dictS == dictT):
        return "TRUE"
    return "FALSE"


s1 = "anagram"
s2 = "nagaram"
print(validAnagramDict(s1, s2))