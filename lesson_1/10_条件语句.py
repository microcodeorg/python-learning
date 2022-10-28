"""
条件语句
"""

if __name__ == '__main__':
    # if / elif / else
    check = 3 - 1  # 2
    list1 = ""

    if list1:  # 1
        print("I am True !")

    elif check == 2:  # 2
        print("I am 1 ==1 !")

    else:  # 3
        print("else")

    print("Hello")

    pass

    # 嵌套
    if True:
        if True:
            pass
        else:
            if True:
                pass
            else:
                pass
    else:
        pass

    # 3目运算
    ab = 1 if False else 0
