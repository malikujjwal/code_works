def maxFruitsBasket(fruits):
    distinctFruits = 0
    subArr = []
    fruitCap = 0
    for i in range(0, len(fruits)):
        if fruits[i] not in subArr:
            distinctFruits += 1

        subArr.append(fruits[i])
        
        fruitCap = max(fruitCap, len(subArr)) if distinctFruits <= 2 else fruitCap
        while distinctFruits > 2:
            fruit = subArr.pop(0)
            if fruit not in subArr:
                distinctFruits -= 1

    return fruitCap

print(maxFruitsBasket([0,1,2,2]))