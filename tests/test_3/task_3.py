def get_num(a, b):
    def sum_num(x, y):
        return x + y
    return sum_num(a, b) + 5


print(get_num(1, 2))
res = get_num(3, 2)
print(res)
