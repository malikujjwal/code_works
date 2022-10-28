def intervalIntersection(firstList, secondList):
    startfirst, startSecond = 0, 0
    result = []
    while startfirst < len(firstList) and startSecond < len(secondList):
        
        if (firstList[startfirst][1] >= secondList[startSecond][0] and firstList[startfirst][0] <= secondList[startSecond][0]) or (firstList[startfirst][0] <= secondList[startSecond][1] and firstList[startfirst][0] >= secondList[startSecond][0]):
            result.append([max(firstList[startfirst][0], secondList[startSecond][0]), min(firstList[startfirst][1], secondList[startSecond][1])])
            
        if firstList[startfirst][1] > secondList[startSecond][1]:
            startSecond += 1
        elif firstList[startfirst][1] == secondList[startSecond][1]:
            startSecond += 1
            startfirst += 1
        else:
            startfirst += 1
            
    
    return result

print(intervalIntersection([[0,2],[5,10],[13,23],[24,25]], [[1,5],[8,12],[15,24],[25,26]]))

# [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]