sec=int(input("Введите количество секунд:"))
min=0
hr=0
day=0
if sec>59:
    min = int(sec/60)
    sec = sec-min*60
    if min > 59:
        hr = int(min / 60)
        min -= hr * 60
        if hr > 23:
            day = int(hr / 24)
            hr -= day * 24
            print(str(day) + ":" + str(hr) + ":" + str(min) + ":" + str(sec))
        else:
            print(str(hr) + ":" + str(min) + ":" + str(sec))
    else:
        print(str(min)+":"+str(sec))
else:
    print("Есть только секунды:", sec)