"""

需求：
    如果年龄小于18，为童工，不合法；
    如果年龄在18-60之间，为合法工作年龄；
    如果年龄大于60,为退休年龄

"""

"""
步骤：
1、用户输入自己的年龄，保存变量 --str；
2、if做判断 elif；
3、输出提示信息，您输入的年龄是X，合法与否；


"""
# age = int(input('请输入您的年龄'))
# if age < 18:
#     print(f'{age}岁为童工，不合法')
#
# elif 18 <= age <= 60:
#     print(f'{age}岁为合法工作年龄')
#
# else:
#     print(f'{age}岁为退休年龄')


"""
需求
1、出拳
  玩家：手动输入
  电脑：1、固定  2、随机
2、判断输赢
   2.1玩家赢
   2.2电脑赢
   2.3平局
"""

# 1.出拳
# 玩家

# import random
#
# player = int(input('请出拳：0--石头， 1--剪刀， 2--布'))
# # 电脑
#
# computer = random.randint(0, 2)
# print(computer)

# 2.判断输赢
# # 玩家获胜：
# if ((player == 0) and (computer == 1) or ((player == 1) and (computer == 2)) or ((player == 2) and (computer == 0))):
#     print('玩家获胜')
# elif player == computer:
#     print('平局')
#
# else:
#     print('电脑获胜')

"""
需求
while 循环练习
"""
# i = 0
# while i < 5:
#     print('你好啊')
#     i += 1
# print('hi，你好')

"""

累加计算100以内的和
"""
#
# i = 1
# res = 0
# while i <= 100:
#     res += i
#     i += 1
# print(res)

