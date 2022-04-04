# Написать функцию, которая будет приниметь одно значение - список.
# Вычислить разницу между максимальным и минимальным значением и вернуть его.

def returnDiff(list: list) -> float:
    maxValue = list[0]
    minValue = list[0]

    for item in list:
        if item >= maxValue:
            maxValue = item

    for item in list:
        if item <= minValue:
            minValue = item

    return maxValue-minValue

#Второй вариант
def returnDiff2(list: list) -> float:
    maxValue = max(list)
    minValue = min(list)

    return maxValue-minValue

numList = [556, 77, 872, 1, 1002.67, 684, 983, 909, 76, 66]
print(returnDiff2(numList))
