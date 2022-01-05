from student import *


class StudentManager(object):
    def __init__(self):
        # 存储学员数据 --列表
        self.student_list = []

    # 一、程序入口函数
    def run(self):
        # 加载学员信息
        self.load_student()
        while True:
            # 显示功能菜单
            self.show_menu()
            # 用户输入功能序号
            menu_num = int(input('请输入需要的功能序号: '))
            if menu_num == 1:
                # 添加学员
                self.add_student()
            elif menu_num == 2:
                # 删除学员
                self.del_student()
            elif menu_num == 3:
                # 修改学员信息
                self.modify_student()
            elif menu_num == 4:
                # 查询学员信息
                self.search_student()
            elif menu_num == 5:
                # 显示所有学员信息
                self.show_student()
            elif menu_num == 6:
                # 保存学员信息
                self.save_student()
            elif menu_num == 7:
                # 退出系统
                break

    # 2.1显示功能菜单 -- 打印序号的功能对应关系 -- 静态方法
    @staticmethod
    def show_menu():
        print('请选择如下功能： ')
        print('1.添加学员')
        print('2.删除学员')
        print('3.修改学员信息')
        print('4.查询学员信息')
        print('5.显示所有学员信息')
        print('6.保存学员信息')
        print('7.退出系统')

    # 2.2添加学员
    def add_student(self):
        # 1、用户输入姓名，性别，手机号
        name = input('请输入姓名： ')
        gender = input('请输入性别： ')
        tel = input('请输入手机号： ')
        # 2、创建学员对象 -- 类？ 类在student文件里面， 先导入student模块，再创建对象
        student = Student(name, gender, tel)
        # 3、将对象添加到学员列表
        self.student_list.append(student)
        print(self.student_list)
        print(student)

    # 2.3删除学员
    def del_student(self):
        # 1.用户输入目标学员姓名
        del_name = input('请输入学员姓名： ')
        # 2.遍历学员列表，如果用户输入的学员存在，则删除学员对象；否则提示学员不存在
        for i in self.student_list:
            if del_name == i.name:
                self.student_list.remove(i)
                break
        else:
            print('该学员不再系统中')
        print(self.student_list)

    # 2.4修改学员信息
    def modify_student(self):
        modify_name = input('请输入学员姓名： ')
        for i in self.student_list:
            if modify_name == i.name:
                i.name = input('请输入学员姓名： ')
                i.gender = input('i请输入学员性别： ')
                i.tel = input('请输入学员的手机号: ')
                print(f'成功修改学员信息，姓名:{i.name}, 性别:{i.gender}, 手机号:{i.tel}')
                break
        else:
            print('该学员不在系统中')

    # 2.5查询学员信息
    def search_student(self):
        search_name = input('请输入学员姓名: ')
        for i in self.student_list:
            if search_name == i.name:
                print(f'该学员的姓名:{i.name}, 性别:{i.gender}, 手机号:{i.tel}')
                break
        else:
            print('该学员不在系统中')

    # 2.6显示所有学员信息
    def show_student(self):
        print(f'姓名\t性别\t手机号')
        for i in self.student_list:
            print(f'{i.name}\t{i.gender}\t{i.tel}')

    # 2.7保存学员信息
    def save_student(self):
        f = open('student.data', 'w')
        new_list = [i.__dict__ for i in self.student_list]
        print(new_list)
        f.write(str(new_list))
        f.close()

    # 2.8加载学员信息
    def load_student(self):
        try:
            f = open('student.data', 'r')
        except:
            f = open('student.data', 'w')
        else:
            data = f.read()
            # 文件中读取的数据都是字符串且字符串内部为字典数据，故需要转换数据类型再转换字典为对象后存储到学员列表--[{}]转换[学员对象]
            new_list = eval(data)
            self.student_list = [Student(i['name'], i['gender'], i['tel']) for i in new_list]
        finally:
            f.close()
