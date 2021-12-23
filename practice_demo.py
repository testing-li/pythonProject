# 第一题

class Person():
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def personInfo(self):
        print(self.name, self.age, self.gender)


p1 = Person('dufu', 21, '男')
p1.personInfo()


# 第二题

class Student(Person):
    def __init__(self, name, age, gender, college, cls):
        super().__init__(name, age, gender)
        self.college = college
        self.cls = cls

    def personInfo(self):
        super().personInfo()
        print(self.college, self.cls)

    def study(self, teacher):
        teacher.teach_obj()
        print(teacher.name + '老师，我学会了')


class Teacher(Person):
    def __init__(self, name, age, gender, college, professional):
        super().__init__(name, age, gender)
        self.college = college
        self.professional = professional

    def personInfo(self):
        super().personInfo()
        print(self.college, self.professional)

    def teach_obj(self):
        print('今天讲了如何对头发进行护理')

    def __str__(self):
        return self.name + ' ' + str(self.age) + ' ' + self.gender + ' ' + self.college + ' ' + self.professional


s = Student('siki', 20, '女', '软件学院', '2班')
# s.personInfo()
t = Teacher('tuoni', 28, '男', '软件学院', '美发')
# t.personInfo()

# s.study(t)
# print(t)
t1 = Teacher('托尼', 10, '男', '软件学院', '美发')
t2 = Teacher('康尼', 20, '女', '测试学院', 'c++')
t3 = Teacher('麦克', 30, '男', '计算机学院', '法律')
l = []
l.append(t1)
l.append(t2)
l.append(t3)
for i in l:
    print(i)
