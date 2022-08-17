line = int(input("Введите сторону квадрата:"))
square = line * line
perimeter = (line + line) * 2
diagonal = line * (2 ** 0.5)
print("Площадь квадрата:", square, "Периметр:", perimeter, "Диагональ:", diagonal)