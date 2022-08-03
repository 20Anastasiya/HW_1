_dict = {'Маргарита':5, 'Ром':8, 'Виски':2, 'Абсент':1, 'Голубая лагуна':5, 'Текила':10}
cash = int(input('Введите сумму:'))
for key, value in _dict.items():
    if cash > value:
        print(key)
