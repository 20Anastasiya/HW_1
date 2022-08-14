_string = '125495384622165'
_dict = {}
sort_dict = {}
for i in _string:
    _dict[i] = _string.count(i)
for i in sorted(_dict.values())[4:0:-1]:
    for k in _dict.keys():
        if _dict[k] == i:
            sort_dict[k] = _dict[k]
print(sort_dict)
