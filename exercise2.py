# Написать функцию, которая будет приниметь одно значение с логическими типы, а затем ковертировать их в строковые
# 'True' и 'False' и возвращать эти значения.

def booleanConvert(flag: bool) -> str:
    if flag == True:
        return 'True'
    else:
        return 'False'


print(booleanConvert(True))
print(booleanConvert(False))
