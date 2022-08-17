_list1 = [1, 2, 7, 'wow', 10, 'yes', 10]
_list2 = [7, 8, 14, 'no', 'yes', 10, 10]
_list3 = []
proverka = ''
for i in range(len(_list1)):
    for j in range(len(_list2)):
        if _list1[i] == _list2[j]:
            _list3.append(_list1[i])
for k in range(len(_list3)):
    while _list3[k].count() > 1:
        _list3.remove(_list3[k])
print(_list3)
