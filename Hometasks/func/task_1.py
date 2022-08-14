def sum_range(start, end):
    result = 0
    if start > end:
        start, end = end, start
    for item in range(start, end+1):
        result += item
    return result
try:
    num_1 = int(input('Введите первое значение',))
    num_2 = int(input('Введите второе значение',))
except TypeError as e:
    print(e, 'Вы ввели неверное значение')
print(sum_range(num_1, num_2))
