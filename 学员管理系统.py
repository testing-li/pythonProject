# 定义函数功能页面
def info_print():
    print("请选择功能-----")
    print('1.添加学员')
    print('2.删除学员')
    print('3.修改学员')
    print('4.查询学员')
    print('5.显示所有学员')
    print('6.退出系统')
    print('-' * 20)


# 等待存储所有学员信息
info = []


def add_info():
    """添加学员信息"""
    # 1 用户输入： 学号、姓名、手机号
    new_id = input('请输入学号：')
    new_name = input('请输入姓名： ')
    new_phone = input('请输入手机号： ')

    # 2 判断是否添加这个学员，如果存在学员姓名，报错提示；如果不存在添加该学员信息
    global info
    # 2.1 不允许姓名重复：判断用户输入的姓名和列表里字典的对应的name相等，提示
    for i in info:
        if new_name == i['name']:
            print("此用户已存在")
            # 退出当前函数，后面添加信息的代码不执行
            return

    # 2.2 如果输入的姓名不存在，添加数据，准备空字典，字典新增数据，列表追加字典
    info_dict = {}

    # 字典新增数据
    info_dict['id'] = new_id
    info_dict['name'] = new_name
    info_dict['phone'] = new_phone
    # print(info_dict)

    # 列表追加字典
    info.append(info_dict)
    print(info)


# 删除学员
def del_info():
    """删除学员函数"""
    # 1。用户输入要删除的学员的姓名
    del_name = input('请输入姓名: ')
    # 2。判断该学员是否存在，存在则删除，不存在则提示
    # 2.1声明info是全局变量
    global info
    # 2。2 遍历列表
    for i in info:
        # 2。3 判断学员是否存在，存在执行删除(列表里面的字典)， break：这个系统不允许重名，删除了一个后面的不需要再进行遍历操作
        if del_name == i['name']:
            # 列表删除数据 --按数据删除remove
            info.remove(i)
            print(f'成功删姓名为{del_name}的学员')
            break
    else:
        print('该用户不在系统中')
    print(info)


# 修改学员信息
def modify_info():
    """修改学员信息函数"""
    # 1 输入要修改的学员姓名
    modify_name = input('输入姓名： ')

    # 2 判断学员是否存在： 存在修改手机号，不存在，提示
    # 2。1 声明info 为全局
    global info
    # 2。2 遍历列表，判断输入的姓名==字典['name']
    for i in info:
        if modify_name == i['name']:
            # 将phone对应的值修改，并终止该循环
            i['phone'] = input('请输入新的手机号: ')
            break
    else:
        print(f'{modify_name}学员不在该系统')
    # 3 打印 info
    print(info)


# 搜索学员信息
def search_info():
    search_name = input('请输入姓名： ')
    global info
    for i in info:
        if search_name == i['name']:
            print('查找的学员信息如下：-----------------')
            print(f'该学员的学号是{i["id"]},姓名是{i["name"]}，手机号是{i["phone"]}')
            break
    else:
        print(f"{search_name}学员不在该系统中")


# 显示所有：
def print_all():
    """显示所有学员信息"""
    print("学号\t姓名\t手机号")
    # 打印所有学员的数据
    for i in info:
        print(f"{i['id']}\t {i['name']}\t {i['phone']}")


while True:
    # 1.显示功能界面
    info_print()

    # 2. 用户输入功能序号
    user_num = int(input('请输入序列号： '))

    if user_num == 1:
        add_info()

    elif user_num == 2:
        # print('删除')
        del_info()
    elif user_num == 3:
        # print('修改')
        modify_info()
    elif user_num == 4:
        # print('查询')
        search_info()
    elif user_num == 5:
        # print('显示所有')
        print_all()
    elif user_num == 6:
        # print('退出系统')
        exit_flag = input('确定要退出吗？ yes or no   ')
        if exit_flag == "yes":
            break
    else:
        print('输入的功能序号有误，请重新输入： ')
