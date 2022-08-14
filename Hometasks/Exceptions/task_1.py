num_1 = input('Введите значение:',)
num_2 = input('Введите значение:',)
try:
    int(num_1)
    int(num_2)
except ValueError:
    print(str(num_1) + str(num_2))
else:
    print(num_1 + num_2)
