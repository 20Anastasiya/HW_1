a = int(input("Введите число а:"))
b = int(input("Введите число b:"))
c = int(input("Введите число c:"))
d = b ** 2 - 4 * a * c
if d > 0:
    x1 = (-b + d ** (1 / 2)) / (2 * a)
    x2 = (-b - d ** (1 / 2)) / (2 * a)
    print(f"x1 = {x1}, x2 = {x2}")
elif d == 0:
    x = -b / (2 * a)
    print(f"x = {x}")
else:
    print("Нет корней!")
