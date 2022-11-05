"""
循环语句
重复执行代码
"""


def fn_while():
    """
    while 循环
    条件循环
    """
    stop = 0
    while stop < 5:
        print(stop)
        stop += 1

    print("stopped")


def fn_for_in():
    """
    for ... in 循环
    range python 内置函数
    计数循环
    """
    for num in range(10):
        print(num)


def fn_for_list():
    """
    遍历 list
    """
    list_1 = ["a", "b", "c"]
    for c in list_1:
        print(c)


def fn_for_dict():
    """
    遍历 dict
    """
    dict_1 = {"a": 1, "b": 2}
    for c in dict_1:
        print("只打印Key", c)

    for key, value in dict_1.items():
        print(f"key: {key}, value: {value}")


def fn_break():
    """
    关键字: break
    作用: 跳出循环体
    """
    for num in range(10):
        if num > 5:
            break

        print("num:", num)

    print("here")


def fn_continue():
    """
    关键字: continue
    作用: 跳过本次循环
    """
    for num in range(10):
        if num == 5:
            continue

        print("num:", num)

    print("here")


if __name__ == '__main__':
    # fn_while()
    # fn_for_in()
    # fn_for_list()
    # fn_for_dict()
    # fn_continue()
    # fn_break()
    pass
