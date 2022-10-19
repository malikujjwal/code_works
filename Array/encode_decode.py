def encode(strs):
    res = ""
    for s in strs:
        res = res + "#" + s

    return res + "#"

def decode(strs):
    res = []
    i = 1
    while i < len(strs):
        j = i
        while(strs[j] != "#"):
            j+=1

        res.append(strs[i:j])
        i = j + 1
    return res

print(encode(["lint","code","love","you"]))
print(decode("#lint#code#love#you#"))