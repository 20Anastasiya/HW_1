import time
def dec(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func()
        end = time.time()
        print('Время выполнения: {} секунд.'.format(end - start), str(func), str(*args), str(**kwargs))
    return wrapper
@dec
def sum_range():
    start = 10
    end = 3
    result = 0
    if start > end:
        start, end = end, start
    for item in range(start, end+1):
        result += item
    return result

sum_range()
