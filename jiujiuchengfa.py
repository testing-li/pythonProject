# # # 九九乘法
# #
# # for i in range(1, 10):
# #     for j in range(1, i + 1):
# #         print(i, '*', j, '=', i * j, end=' ')
# #     print()
#
# # 素数
# #
# # res = int(input("请输入一个大于1的整数："))
# #
# # isSu = True
# # for i in range(2, res):
# #     if res % i == 0:
# #         isSu = False
# #         # break
# #         # print(res ,"不是素数")
# #
# # if isSu:
# #     print(res, '是素数')
# #
# # else:
# #     print(res, '不是素数')
#
#
# # 拆分三位数
#
# # n = int(input("请输入一个三位数："))
# # ge = n % 10
# # bai = int(n / 100)
# # shi = int(n / 10) % 10
# # print('个位数是：', ge)
# # print('十位数是：', shi)
# # print('百位数是：', bai)
#
# # 水仙花数
#
#
# # n = int(input("请输入一个三位数："))
#
# # print('个位数是：', ge)
# # print('十位数是：', shi)
# # print('百位数是：', bai)
# # l = []
# # for n in range(100, 1000):
# #     ge = n % 10
# #     bai = int(n / 100)
# #     shi = int(n / 10) % 10
# #     if n == (ge ** 3 + shi ** 3 + bai ** 3):
# #         l.append(n)
# # print(l)
#
# # 求8的阶乘
# # res = 1
# # for i in range(1, 9):
# #     res *= i
# # print(res)
#
# # # 求1！+2！+3！+....+20!的和
# # he = 0
# # for i in range(1, 21):
# #     res = 1
# #     for j in range(1, i + 1):
# #         res *= j
# #     he += res
# # print(he)
#
# # 继承
# class Person():
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def eat(self):
#         print(self.name + '正在吃饭')
#
#     def sleep(self):
#         print(self.name + '正在睡觉')
#
#
# p1 = Person('siki', 20)
# p1.eat()
# p1.sleep()
#
#
# class Teacher(Person):
#     def __init__(self, name, age, title):
#         super().__init__(name, age)
#         self.title = title
#
#     def teach(self):
#         print(self.name + '正在教书')
#
#     # 重写方法
#     def eat(self):
#         print(self.name + '去食堂吃饭')
#
#
# t1 = Teacher('libai', 25, '高级教师')
# t1.eat()
# t1.teach()


# 游戏RGB
import weapon


class Role():
    def __init__(self, name, lv, role_type, damage, bullet_count):
        """

        :param name: 英雄名字
        :param lv:   等级
        :param role_type: 角色类型
        :param damage:  攻击力
        :param bullet_count: 子弹数量
        :return:
        """
        self.name = name
        self.Lv = lv
        self.role_type = role_type
        self.weapon = weapon.Weapon(damage, bullet_count)

    def move(self):
        print(self.name + '正在走路')

    def attack(self):
        self.weapon.attack()


role = Role('siki', 10, '魔法师', 20, 20)
role.move()
role.attack()
