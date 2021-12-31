# 需求  0-10之间的偶数列表

# list1 = [i for i in range(10) if i % 2 == 0]
# print(list1)

# 多个for循环实现列表推导式
# [(1, 0),(1, 1),(1, 2),(2, 0),(2, 1),(2, 2)]

list1 = [(i, j) for i in range(1, 3) for j in range(3)]
print(list1)

# 字典推导式

dict1 = {i: i ** 2 for i in range(1, 5)}
print(dict1)

list1 = ['name', 'age', 'gender']
list2 = ['Tom', 20, 'nan']
dict3 = {list1[i]: list2[i] for i in range(len(list2))}
print(dict3)

# 集合推导式
list1 = [1, 1, 2]
set1 = {i ** 2 for i in list1}
print(set1)


