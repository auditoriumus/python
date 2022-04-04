# Написать функцию, которая будет принимать одно значение - строку или список. Необходимо зашифровать строку.
# Первый элемент строки - код буквы в ascii (например 'a' = 97, a 'A' = 65). Следующий элемент - закодированная
# с помощью таблицы разница между текущим и предыдущим символом, итд. Если подается список - необходимо расшифровать его.
# Алгоритм такой же - первое число перекодируется в соответствием с таблицей ascii, второй символ - сумма первого и
# второго числа перекодированная с помощью таблицы ascii.

def codeAscii(characters):
    if isinstance(characters, str):
        result = []
        i = 0
        for letter in characters:
            code = ord(letter)
            if i == 0:
                result.append(code)
            else:
                codePrev = ord(characters[i-1])
                result.append(code - codePrev)
            i += 1
    elif isinstance(characters, list):
        result = ''
        i = 0
        for el in characters:
            if i == 0:
                let = chr(el)
                result += let
            else:
                prev = ord(result[i-1])
                code = prev + characters[i]
                result += chr(code)
            i += 1
    return result

print(codeAscii("Hello"))
print(codeAscii([ 72, 33, -73, 84, -12, -3, 13, -13, -68 ]))
