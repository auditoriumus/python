# Создать функции, которая будет строить лестницу, используя знаки ‘_’ и ‘#’.
# Положительное значение обозначают, что направление лестницы направленно вверх и вниз для отрицательных значений.

def staircase(floor: int) -> str:
    floorCount = abs(floor)
    i = 0
    string = ''
    while i < floorCount:
        if floor > 0:
            string += (floorCount - i) * '#' + i * '_' + '\n'
        elif floor < 0:
            string += i * '_' + (floorCount - i) * '#' + '\n'
        i += 1
    return string[::-1]


print(staircase(5))
print(staircase(-9))
