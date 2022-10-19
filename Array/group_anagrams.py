from collections import defaultdict

def groupAnagrams(strArr):
    anagramDict = defaultdict(list)

    for str in strArr:
        alphabetArr = [0] * 26

        for s in str:
            alphabetArr[ord(s) - ord("a")] += 1
        anagramDict[(tuple(alphabetArr))].append(str)
    
    return anagramDict.values()
    
strs = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strs))
