# Написать функцию, которая будет принимать одно значение - список. Функция должна возвращать самое
# частое значение в списке (встречается > N/2). Пример: test_function(["A", "A", "A", "B", "C", "A"]) ➞ "A"

characters = ["A", "A", "A", "B", "C", "A", "C", "C", "C", "A", "C"]


def findOftenValue(list: list):
    dict = {}
    for item in list:
        if dict.get(item) is None:
            dict.update({item: 1})
        else:
            value = dict.get(item)
            value += 1
            dict.update({item: value})

    count = 0
    for key in dict:
        if dict[key] > count:
            count = dict[key]
    result = {}
    for key in dict:
        if dict[key] == count:
            result[key] = dict[key]

    return result


print(findOftenValue(characters))
