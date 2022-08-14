import string
def pangramma(word, alphabet = string.ascii_lowercase):
    word = set(word.lower())
    alphabet = set(alphabet)
    if word.issubset(alphabet):
        return 'Это панграмма'
    else:
        return 'Это не панграмма'
try:
    word = input('Введите слово или строку: ')
except ValueError as exp:
    print(exp, 'Вы ввели неверное значение')
print(pangramma(word))
