# Напишите функцию, которая принимает два значения - числа num, length (основное число, количество умножений).
# Функция должна возвращать список перемножений числа num length раз. Пример: test_function(7, 5) ➞ [7, 14, 21, 28, 35]

def multiply(num: float, length: int) -> list:
    list = []
    for i in range(1, length + 1):
        list.append(num * i)
    return list

print(multiply(5,5))
