def evalRPN(tokens):
    stack = []
    for val in tokens:
        if val == "+":
            twoSum = stack.pop() + stack.pop()
            stack.append(twoSum)
        
        elif val == "-":
            i,j = stack.pop(), stack.pop()
            diff = j - i
            stack.append(diff)
            
        elif val == "*":
            prod = stack.pop() * stack.pop()
            stack.append(prod)
            
        elif val == "/":
            i,j = stack.pop(), stack.pop()
            stack.append(int(float(j) / float(i)))
            
        else:
            stack.append(int(val))
    
    return stack[0]

print(evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))