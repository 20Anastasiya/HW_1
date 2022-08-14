_list1 = [15, 14, 3, 0, 9, 66, 7, 0, 723, 89, 56, 2980, 3580]
_list2 = [77, 5, 2, 45, 0, 6, 9, 3, 1, 5, 68, 2, 5, 2650, 978]
_set1, _set2 = set(_list1), set(_list2)
_result = list(_set1.intersection(_set2))
_result.sort()
print(_result)
# for i in range(len(_list1)):
#     if _list1[i] in _list2 and _list1[i] not in _result:
#         _result.append(_list1[i])
