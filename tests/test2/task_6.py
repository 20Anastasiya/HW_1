_dict = {'Маргарита':5, 'Ром':8, 'Виски':2, 'Абсент':1, 'Голубая лагуна':5, 'Текила':10}
while True:
    try:
        cash = int(input('Введите сумму:'))
        if cash == 0:
            raise ValueError
    except ValueError as exc:
        print(exc)
        print('Ошибка ввода!')
    else:
        break
for key, value in _dict.items():
    if cash > value:
        print(key)
