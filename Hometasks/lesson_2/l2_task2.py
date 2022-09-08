num=list(input("Ввелите трёхзначное число:"))
proverka=len(num)
if proverka==3:
    num1=int(num[0])
    num2=int(num[1])
    num3=int(num[2])
    sum=num1+num2+num3
    print("Сумма равна:", sum)
else:
    print("Вы ввели неверное значение!")