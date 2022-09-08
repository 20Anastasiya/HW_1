_string = 'asdf8g5h12bn3 7s56h8g4h10l7'
_list = []
_string1 = ''
# _string = _string.replace('')
for i in range(len(_string)):
    if _string[i].isalpha():
        _string1 += ' '
    else:
        _string1 += _string[i]
_list = _string1.split(' ')
while _list.count('') > 0:
    _list.remove('')
for j in range(len(_list)):
    _list[j] = int(_list[j])
print(_string1)
print(_list)
