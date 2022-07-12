first_tup = (5, 4, 8, 'oh', 'hey', 10, 7, 12, 5, 7, )
second_tup = (5, 6, 14, 'oh', 'yes', 0, 7, 12, )
twice = []
for i in range(len(first_tup)):
    for j in range(len(second_tup)):
        if first_tup[i] == second_tup[j] and first_tup[i] not in twice:
            twice.append(first_tup[i])
for k in twice:
    while twice.count(k)>1:
        twice.remove(k)
print(twice)
