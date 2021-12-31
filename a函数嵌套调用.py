# 打印一条横线
def print_line():
    print('-' * 20)


# 打印多条横线
def print_lines(num):
    i = 0
    while i < num:
        print_line()
        i += 1


print_lines(5)


# 三个数求和
def sum_num(a, b, c):
    return a + b + c


result = sum_num(1, 2, 3)
print(result)


# 求三个数的平均值
def avg_num(a, b, c):
    sum_result = sum_num(a, b, c)
    return sum_result / 3


result = int(avg_num(1, 2, 3))
print(result)
