# 父类，
class Master(object):
    def __init__(self):
        self.kongfu = '[古法煎饼果子配方]'

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')


# 子类 继承父类
class Prentice(Master):
    pass


# 使用徒弟创建对象，调用实例属性方法
daqiu = Prentice()
print(daqiu.kongfu)
daqiu.make_cake()