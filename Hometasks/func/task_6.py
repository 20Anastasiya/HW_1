def custom_ange(start, end, step=1):
    if start > end:
        start, end = end, start
    _list = list(range(start, end))
    #for number in _list[start, end, step]:
    yield _list[start, end, step]
try:
    start = int(input('Введите первое значение',))
    end = int(input('Введите второе значение',))
    step = int(input('Введите третье значение', ))
except TypeError as e:
    print(e, 'Вы ввели неверное значение')
generator = custom_ange(start, end, step)
for item in generator:
    print(item)
