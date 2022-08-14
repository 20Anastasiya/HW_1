from collections.abc import Hashable
my_list = ['п', 'р', 'о', 'б', 'а', 'cat', [8, 4, 6], ['a']]
_set = set()
for item in my_list:
    l = lambda item: item if isinstance(item, Hashable) else ''
    _set.add(l)  #не получилось перевести результат в читаемый язык
print(_set)
