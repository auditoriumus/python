# Напишите функцию, который имеет два аргумента - x и y. Функция должна выводить координатный угол,
# в котором находятся координаты (x, y). Точки внутри координатного угла I имеют положительные абсциссы и ординаты.
# Точки внутри координатного угла II имеют отрицательные абсциссы и положительные ординаты.
# Точки внутри координатного угла III имеют отрицательные абсциссы и ординаты Точки внутри координатного угла IV имеют
# положительные абсциссы и отрицательные ординаты.

def returnAngleNumber(x: float, y: float) -> int:
    if x == 0 or y == 0:
        return False
    elif x > 0:
        if y > 0:
            return 'I'
        else:
            return 'IV'
    else:
        if y > 0:
            return 'II'
        else:
            return 'III'


print(returnAngleNumber(1, 0))
print(returnAngleNumber(1, 2))
print(returnAngleNumber(-1, 2))
print(returnAngleNumber(-1, -2))
print(returnAngleNumber(1, -2))
