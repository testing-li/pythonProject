# 父类，
class Master(object):
    def __init__(self):
        self.kongfu = '[古法煎饼果子配方]'

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')


# 创建学校类
class School(object):
    def __init__(self):
        self.kongfu = '[测试版煎饼果子配方]'

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')


# 子类 继承父类(学校类，师傅类)，添加和父类同名的属性和方法
class Prentice(School, Master):
    def __init__(self):
        self.kongfu = '[独创的煎饼果子配方]'

    def make_cake(self):
        self.__init__()
        print(f'运用{self.kongfu}制作煎饼果子')

    def make_master_cake(self):
        Master.__init__(self)
        Master.make_cake(self)

    def make_school_cake(self):
        School.__init__(self)
        School.make_cake(self)


# 徒孙类, 多层继承
class Tusun(Prentice):
    pass


# 使用徒弟创建对象，调用实例属性方法
daqiu = Prentice()
# print(daqiu.kongfu)
daqiu.make_cake()
daqiu.make_master_cake()
daqiu.make_school_cake()

zhangsan = Tusun()
zhangsan.make_cake()
zhangsan.make_master_cake()
zhangsan.make_school_cake()