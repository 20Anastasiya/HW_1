import math
line_a=int(input("Введите длину первой стороны треугольника:", ))
line_b=int(input("Введите длину второй стороны треугольника:", ))
line_c=int(input("Введите длину третьей стороны треугольника:", ))
if line_a+line_b<line_c or line_a+line_c<line_b or line_b+line_c<line_a:
    print("Вообще-то такого треугольника не существует...")
else:
    p=(line_a+line_b+line_c)/2
    square=math.sqrt(p*(p-line_a)*(p-line_b)*(p-line_c))
    print("Площадь заданного треугольника равна:", square)