tuple_from_user = tuple(input('Введите значения: '))
counter = 0
res = []
for i in tuple_from_user:
    counter = tuple_from_user.count(i)
    if (i + f': {counter}') not in res:
        res.append(i + f': {counter}')
    counter = 0
print(res)
