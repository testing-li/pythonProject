# 需求主线：
"""
1、被烤的时间和对应的地瓜状态：
0-3分钟：生的
3-5分钟：半生的
5-8分钟：熟的
超过8分钟：烤糊了

2、添加的调料：
用户可以按照自己的意愿添加调料

"""


# 1、 定义类：初始化属性，被烤和添加调料的方法、展示对象显示信息的str
class SweetPotato():
    def __init__(self):
        """
        被烤时间
        烤的状态
        调料列表
        """
        self.cook_time = 0
        self.cook_state = "生的"
        self.condiments = []

    def cook(self, time):
        """

        :param time:  计算烤地瓜的时间
        :return:
        """
        self.cook_time += time
        if 0 <= self.cook_time < 3:
            self.cook_state = "生的"
        elif 3 <= self.cook_time < 5:
            self.cook_state = "半生不熟的"
        elif 5 <= self.cook_time < 8:
            self.cook_state = "熟了"
        elif self.cook_time >= 8:
            self.cook_state = "烤糊了"

    def add_condiments(self, condiment):
        # 用户意愿的调料追加到调料列表
        self.condiments.append(condiment)

    def __str__(self):
        return f"这个地瓜烤了{self.cook_time},状态是{self.cook_state}，调料有{self.condiments}"


# 2、创建对象并调用对应的实例方法
digua1 = SweetPotato()

digua1.cook(2)
digua1.add_condiments('辣的')
print(digua1)

digua1.cook(2)
digua1.add_condiments('带有酱油')
print(digua1)
