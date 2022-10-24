def isNumberHappy(num):
    slow, fast = num, num

    while True:
        slow = squareNumber(slow)
        fast = squareNumber(squareNumber(fast))
        if slow == fast:
            break
    
    return slow == 1

def squareNumber(num):
    squareNum = 0
    while num > 0:
        digit = num % 10
        squareNum += digit * digit 
        num //= 10

    return squareNum

print(isNumberHappy(23))