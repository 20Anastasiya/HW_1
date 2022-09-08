numbers = [4, 5, 6, 2, 0, 12, 7]
summa_1 = 0
summa_2 = 0
for i in range(len(numbers)):
    summa_1 += numbers[i]
print(summa_1)
n = 0
while n < len(numbers):
    summa_2 += numbers[n]
    n += 1
print(summa_2)
