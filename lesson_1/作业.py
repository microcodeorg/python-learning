"""
作业
"""


def square():
    # square_w 为正方形的边长，
    # 创建一个名为 'square_area' 的变量，等于以square_w为边长的正方形面积，并打印。
    square_w = 2
    print("square_area=")


def oblong():
    # oblong_w, oblong_h 分别为长方形的宽和高
    # 创建一个名为 'oblong_area' 的变量，等于长方形面积，并打印。
    oblong_w, oblong_h = 6, 3
    print("oblong_area=")


def circular():
    # circular_diameter 为圆的直径
    # 创建一个名为 'circular_radius'，等于圆的半径，并打印。
    # 创建一个名为 'circular_area'，等于圆的面积，并打印。
    pi = 3.14159
    circular_diameter = 3

    print("circular_radius=")
    print("circular_area=")


def print_multiplication_table():
    # 用循环和运算的方式打印 99乘法表，输出格式如下
    # 1x1=1
    # 1x2=2 | 2x2=4
    # 1x3=3 | 2x3=6 | 3x3=9
    pass


def print_abcdef():
    # 使用for循环，依次打印字符串"abcdef"中的每个字符。
    pass


def print_my_name_card():
    # 使用字符串的格式化输出完成以下名片的显示，只要求格式，信息随便填。
    """
    ==========我的名片==========
    姓名:     itheima
    QQ:      xxxxxxx
    手机号:   185xxxxxx
    公司地址: 北京市xxxx
    ===========================
    """
    pass


def filter_name():
    # 使用列被生成式，过滤并打印出姓'李'的名字
    names = ["李白", "吴小", "李红", "张三", "李四"]
    pass


if __name__ == '__main__':
    square()
    oblong()
    circular()
    print_multiplication_table()
    print_abcdef()
    print_my_name_card()
    filter_name()
