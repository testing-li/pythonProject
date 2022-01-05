"""
需求：
1。定义类：私有属性，类方法获取这个私有类属性
2.创建对象，然后调用类方法
"""


class Dog(object):
    __tooth = 10

    # 定义类方法
    @classmethod
    def get_tooth(cls):
        return cls.__tooth


wangcai = Dog()
res = wangcai.get_tooth()
print(res)