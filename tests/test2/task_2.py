from random import randint
_list = [randint(0, 10) for i in range(100)]
_list = set(_list)
_list = sorted(tuple(_list), reverse=True)
print(_list)
