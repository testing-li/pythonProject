# 自定义异常
class ShortInputError(Exception):
    def __init__(self, length, min_len):
        self.length = length
        self.min_len = min_len

    # 设置抛出异常的描述信息
    def __str__(self):
        return f'你输入的长度是{self.length}, 不能少于{self.min_len}个字符'


def main():
    # 抛出异常
    try:
        con = input('请输入密码： ')
        if len(con) < 3:
            raise ShortInputError(len(con), 3)
    # 捕获异常
    except Exception as result:
        print(result)
    else:
        print('密码已经输入完成')


main()
