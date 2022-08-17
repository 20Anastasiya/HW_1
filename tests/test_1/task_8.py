numb = [4, 2, 6, 12, 8, 7]
for i in range(len(numb)-1):
    for j in range(len(numb)-1):
        if numb[j] > numb[j+1]:
            numb[j], numb[j+1] = numb[j+1], numb[j]
print(numb)
