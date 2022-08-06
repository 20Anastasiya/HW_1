_list = [98, 9, 4, 3478, 39, 8, 'r', 0]
while True:
    try:
        num = int(input('Введите делитель: '))
    except Exception as e:
        print(e)
    else:
        break
for item in _list:
    try:
        a = num/item
    except TypeError:
        print('Возникла ошибка типа')
    except ZeroDivisionError:
        print('Ошибка деления на ноль. Цикл будет прерван.')
        break
    except Exception as exc:
        print(exc)

