# Написать функцию, которая будет принимать одно значение - список. Список содержит числа. Все числа,
# кроме двух, повторяются как минимум два раза. Вернуть список из этих двух неповторяющихся чисел

def findUnrepeat(numbers: list):
    unrepeat = []
    for item in numbers:
        if item in unrepeat:
            unrepeat.remove(item)
        else:
            unrepeat.append(item)
    return unrepeat

list = [1,2,3,4,5,6,7,5,4,3,2,1]
print(findUnrepeat(list))
