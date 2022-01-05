class Student(object):
    def __init__(self, name, gender, tel):
        """

        :param name:
        :param gender:
        :param tel:
        """
        self.name = name
        self.gender = gender
        self.tel = tel

    def __str__(self):
        return f'{self.name}, {self.gender}, {self.tel}'

# aa = Student('aa', 'nv', 11)
# print(aa)
