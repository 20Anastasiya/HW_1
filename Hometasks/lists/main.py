spis1 = ['hi', 'little', '', 'girl', '']
print(spis1)
while '' in spis1:
    spis1.remove('')
print(spis1)


# spis2 = [4, 12, 6, 8, 3, 7, 5, 9, 2]
# print(spis2)
# spis2 = [i ** 2 for i in spis2]
# print(spis2)

# spis3 = [20, 12, 14, 0, 15, 9, 20, 34, 52, 20, 4]
# print(spis3)
# while 20 in spis3:
#     spis3.remove(20)
# print(spis3)

# spis4 = [20, 12, 14, 0, 15, 9, 20, 34, 52, 20, 4]
# spis4.reverse()
# print(spis4)

# spis5 = [20, 12, 14, 0, 15, 9, 20, 34, 52, 20, 4]
# min_item = min(spis5)
# max_item = max(spis5)
# for i in range(len(spis5)):
#     if spis5[i] == min_item:
#         spis5[i] = max_item
#     elif spis5[i] == max_item:
#         spis5[i] = min_item
# print('Min item:', min_item)
# print('Max item:', max_item)
# print(spis5)

# spis6 = [20, 12, 14, 0, 12, 9, 20, 34, 52, 0, 4]
# povtor = []
# for symbol in range(len(spis6)):
#     if spis6.count(spis6[symbol])>1:
#         if spis6[symbol] not in povtor:
#             povtor.append(spis6[symbol])
# print(povtor)

# spis7 = [2, 6, 3, 4, 5, 10]
# summa = sum(spis7)
# proizv = 1
# for p in range(len(spis7)):
#     proizv = proizv * spis7[p]
# print(summa)
# print(proizv)

# spis8 = [i for i in range(2,45,2)]
# print(spis8)

# bubble = [20, 12, 14, 0, 12, 9, 34, 52, 0, 4]
# for step in range(len(bubble)-1):
#     for i in range(len(bubble)-1):
#         if bubble[i] > bubble[i+1]:
#             bubble[i], bubble[i+1] = bubble[i+1], bubble[i]
# print(bubble)

# mas = [4, 3, 5, 2, 1, 6, 8]
# for step in range(1, len(mas)):
#     item = mas[step]
#     j = step - 1
#     while j >= 0 and item < mas[j]:
#         mas[j + 1] = mas[j]
#         j = j - 1
#     mas[j + 1] = item
# print(mas)
