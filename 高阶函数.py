# 1.map的使用

# 计算序列中各个数值的2次方
import functools

list1 = [1, 2, 3, 4, 5]


def func1(x):
    return x ** 2


result = map(func1, list1)

print(result)
print(list(result))


def func(a, b):
    return a + b


result = functools.reduce(func, list1)

print(result)

# filter 函数使用

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def func(x):
    return x % 2 == 0


result = filter(func, list1)

print(result)
print(list(result))
