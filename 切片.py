# 切片
name = 'abcdefg'
print(name[0: 3])  # 不包括末尾的数字
print(name[0:5:2])
print(name[::-1])  # 步长为负数时，显示的为倒序

# 字符串常用方法：

# 1.语法  find  index  count  rfind  rindex
str = "hello world welcome to china"
print(str.find('to'))  # 返回字串开始的下标

print(str.index('to'))  # 效果与find相同

print(str.count('to'))  # 统计数量

print(str.rfind('to'))  # 倒序查找，返回的下标仍为正序的下标

print(str.rindex('to'))  # 同上

# 字符串的修改方法  replace split join
name = 'hello world  and welcome to china  and join us'

print(name.replace('and', 'he'))  # 有返回值，不会修改原有的字符串
print(name)

print(name.split('and', 1))  # 返回一个列表，且丢失分割字符

print('.'.join(name))

"""
处理字符串，大小写：
方法： capitalize  title  lower  upper

"""

str = "hello world welcome to python"

print(str.capitalize())  # 第一个字符的首字母大写（后面有大写会变成小写）  Hello world welcome to python

print(str.title())  # 每一个字符的首字母大写  Hello World Welcome To Python
print(str)
name = "CAN YOU SPEAK CHINESE"
print(name.lower())  # 所有字符串的字母均变为小写  can you speak chinese

print(str.upper())  # 所有字符小写变成大写   HELLO WORLD WELCOME TO PYTHON

#  删除首位字符的方法：  lstrip  rstrip strip

name = "   hello world python  "

print(name.lstrip())  # 左侧空字符删除，不改变原有字符
print(name)

print(name.rstrip())  # 右侧空字符删除，不改变原有字符
print(name.strip())  # 左右侧空字符删除，不改变原有字符

# 修改字符串左中右对齐的方法：  ljust   rjust  center
str = "hello"
print(str.ljust(10, '.'))  # 左对齐

print(str.rjust(10, '.'))  # 右对齐

print(str.center(10, '.'))  # 居中

# 判断 字符串常用操作方法，判断开头或者结尾  startswith  endswith   isalpha  isdigit  isalnum  isspace

name = "hello world and welcome to china"

print(name.startswith('he'))  # 返回的是布尔值  True

print(name.endswith('na'))  # 返回的是布尔值  True

mystr1 = 'hello'

print(mystr1.isalpha())  # 字符串至少有一个字符并且所有字符都是字母返回true，否则返回false

print(mystr1.isdigit())  # 如果字符串只包含数字则返回true ，否则返回false

a = ' '
print(a.isspace())  # 空字符串时，返回true

# 判断是否存在于列表中

namelist = ['siki', 'tom', 'lily']

print('tom' in namelist)
print('tom' not in namelist)

# 增加数据
namelist = ['june', 'rose', 'siki']
print(namelist.append('victor'))
print(namelist.extend(['fan', 'mei']))
print(namelist.insert(4, 'chen'))
print(namelist)

# 删除数据
name_list = ['Tom', 'lily', 'rose']
# del namelist
# print(namelist)
# del namelist[1]
# print(namelist)
# print(name_list.pop(1))
# print(name_list)
# name_list.remove('rose')
# print(name_list)

name_list.clear()
print(name_list)