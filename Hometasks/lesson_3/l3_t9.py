money = float(input("Введите количество рублей:"))
year = int(input("Введите срок вклада:"))
temp = 1
while temp <= year:
    money += money * 0.1
    temp += 1
print("Сумма на счету составит:", money)