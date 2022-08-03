from random import randint
_list = [randint(0, 10) for i in range(100)]
_list.sort()
_list = set(_list)
_list = tuple(_list)
print(_list)
