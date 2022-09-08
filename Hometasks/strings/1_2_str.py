# print(' TASK 1:')
# letter = input('Введите строку:').lower()
# symbol = input('Введите символ:')
# num = 0
# for i in letter:
#     if i == symbol:
#         num += 1
# print(num)

print(' TASK 2:')
string_2 = input('Введите строку:').lower()
symbol_2 = input('Введите символ:').lower()
num = range(len(string_2))
result = ""
for j in range(len(string_2)):
    if string_2[j] == symbol_2:
        result += str(j) + " "
        break
for k in reversed(range(len(string_2))):
    if string_2[k] == symbol_2:
        result += str(k) + " "
        break
if result == "":
    print('Такого символа нет в строке')
print(result)


