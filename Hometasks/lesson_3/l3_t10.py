num_1 = int(input("Введите 1 число:"))
num_2 = int(input("Введите 2 число:"))
verb = input("Введите оператор (+  -  *  /  **  %  //):")
result = 0.0
if verb == '+':
    result = num_1 + num_2
    print(result)
elif verb == '-':
    result = num_1 - num_2
    print(result)
elif verb == '*':
    result = num_2 * num_1
    print(result)
elif verb == '/':
    result = num_1 / num_2
    print(result)
elif verb == '**':
    result = num_1 ** num_2
    print(result)
elif verb == '%':
    result = num_1 % num_2
    print(result)
elif verb == '//':
    result = num_1 // num_2
    print(result)
else:
    print("Ошибка ввода!")