def isValid(s):
    if len(s) % 2 != 0:
        return False
    stack = []
    inverse = { "}": "{", ")": "(", "]": "["}
    
    for str in s:
        if str not in inverse:
            stack.append(str)
            continue
        if not stack or stack[-1] != inverse[str]:
            return False
        
        stack.pop()
    
    return not stack

print(isValid("[()]"))