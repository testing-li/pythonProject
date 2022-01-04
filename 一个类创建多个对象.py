# 1、一个类创建多个对象,2.多个对象都调用函数都时候，self 地址是否相同

class Washer():
    def wash(self):
        print('洗衣服')

        # 类里面获取对象属性
    def print_info(self):
        print(self.width)
        print(self.height)


haier1 = Washer()
# 添加对象属性
haier1.width = 300
haier1.height = 500

# 对象调用的方法
haier1.print_info()
haier1.wash()
# 类外面获取对象属性
print(haier1.width)
print(haier1.height)
# haier2 = Washer()
# haier2.wash()
