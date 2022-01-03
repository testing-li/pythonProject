# 计算3以内的数字累加

def sum_numbers(num):
    if num == 1:
        return 1
    return num + sum_numbers(num - 1)


res = sum_numbers(3)
print(res)