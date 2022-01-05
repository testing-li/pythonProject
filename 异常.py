"""
需求：
尝试打开文件
"""
# try:
#     f = open('test.txt', 'r')
# except:
#     f = open('test.txt', 'w')

"""
需求：尝试执行打印异常信息
"""
try:
    # print(1/0)
    print(num)
# except (ZeroDivisionError, NameError) as result:
except Exception as result:    # 捕获所有异常
    print(result)
else:
    print('没有异常时执行的代码')
