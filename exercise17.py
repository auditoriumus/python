# Имеется строк из символов в нижнем регистре ascii[["a".."z"]]. Нужно сократить строку следующим образом:
# берется пара соседних символов и если они одинаковы, то они удаляются. Например aab должно превратится в b.
# Нужно удалить как можно больше символов. Если результирующая строка пустая, нужно вернуть "Empty String"

def deletePair(string: str) -> str:
    i = 0
    result = ''
    while i < len(string):
        if string[i] != string[i + 1]:
            result += string[i]
            i += 1
        else:
            i += 2
        if i == len(string) - 1:
            result += string[i]
            break
        elif i > len(string) - 1:
            break
    return result if result else 'Empty String'


print(deletePair('aaabccddd'))
