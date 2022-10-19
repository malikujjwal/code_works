def topKFrequent(nums, k):
    dict = {}
    freq = [[] for x in range(len(nums)+1)]

    for n in nums:
        dict[n] = 1 + dict.get(n, 0)

    for n,c in dict.items():
        freq[c].append(n)

    kFreq = []
    
    for i in range(len(freq)-1, 0, -1):
        for x in freq[i]:
            kFreq.append(x)
            if(len(kFreq) == k):
                return kFreq


nums = [1]
print(topKFrequent(nums, 1))
