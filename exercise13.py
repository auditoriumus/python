# Написать функцию, которая будет принимать одно значение - строку. Функция определяет свободные и занятые участки пляжа.
# Строка состоит из двух символов 0 - свободный участок, 1 - занятый участок. Из-за недавних ограничений новый человек
# не может занять место рядом с другим. Должно быть одно свободное место между двумя людьми, отдыхающими на пляже.
# Функци должна вернуть число - количество новых людей, которые могут воспользоваться местами на пляже.

def freePlaces(string: str) -> int:
    freePlaces = string.count('0')
    numberOfPersons = string.count('1')
    return freePlaces - numberOfPersons if freePlaces - numberOfPersons >= 0 else 0

print(freePlaces('10101010101010101000'))