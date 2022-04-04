# Написать функцию, которая будет принимать одно значение - список. Функция должна возвращать самое
# частое значение в списке (встречается > N/2). Пример: test_function(["A", "A", "A", "B", "C", "A"]) ➞ "A"

characters = ["A", "A", "A", "B", "C", "A", "C", "C", "C"]


def findOftenValue(list: list) -> str:
    dict = {}
    for item in list:
        if dict.get(item) is None:
            dict.update({item: 1})
        else:
            value = dict.get(item)
            value += 1
            dict.update({item: value})

    count = 0
    resultKey = ''
    for key in dict:
        if dict[key] > count:
            count = dict[key]
            resultKey = key

    return resultKey


print(findOftenValue(characters))
