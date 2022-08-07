_tuple = (1, 2, 8, 7, 5, 4, 4.5, 8)
_list = list(_tuple)
_list.sort()
for i in _list:
    if type(i) is not int:
        print('Найден элемент, не относящийся к типу данных int')
        break
else:
    print(_list)
# chek = True
# for i in range(len(_list)):
#     if type(_list[i]) is int:
#         chek = True
#     else:
#         chek = False
#         break
# print(chek)
# if chek == True:
#     print(_list)
# elif chek == False:
#     print(_tuple)
