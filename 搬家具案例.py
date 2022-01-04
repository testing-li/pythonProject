# 需求：
"""
将小于房子剩余面积的家具放到房子中
"""


class Furniture():
    def __init__(self, name, area):
        """

        :param name:  家具名字
        :param area:  家具占地面积
        """
        self.name = name
        self.area = area


class Home():
    def __init__(self, address, area):
        """

        :param address: 地理位置
        :param area:  房屋面积
        """
        self.address = address
        self.area = area
        self.free_area = area
        self.furniture = []

    def __str__(self):
        return f'房子地理位置在{self.area}, 房子面积是{self.area}, 剩余面积是{self.free_area}, 家具有{self.furniture}'

    def add_furniture(self, item):
        if item.area <= self.free_area:
            self.furniture.append(item.name)
            self.free_area -= item.area
        else:
            print('用户家具太大，剩余面积不足，无法容纳')


# 创建实例
bed = Furniture('双人床', 6)
sofa = Furniture('沙发', 10)

# 房子1，北京， 1000
jia1 = Home('北京', 1000)
print(jia1)

jia1.add_furniture(bed)
print(jia1)

