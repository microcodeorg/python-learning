"""
运算符号
"""


if __name__ == '__main__':
    # 比较运算符 == != > < >= <=
    val = 1  # 赋值
    print(1 == 1)   # True
    print(1 != 1)   # False
    print(1 != 2)   # True

    print(1 > 2)    #
    print(1 < 2)  #
    print(1 >= 2)   #
    print(1 <= 2)   #
    # 错误
    # print(1 =< 2)


    # 赋值运算符 +=
    a = 1
    a += 1
    a -= 2
    a //= 3
    a **= 1
    pass

    # 逻辑运算符 and or(或者) not
    is_sunday = False
    is_monday = True
    # &&
    print(is_monday and is_sunday)  # False
    # ||
    print(is_monday or is_sunday)   # True
    # !
    print(not is_monday)  #
    pass

    # 成员运算符 in / not in
    a1 = "a"
    str1 = "abc"
    print(a1 in str1) # True

    print(1 not in [1, 2, 3]) # True
    print("刘备" not in {"张飞": 1})  # False

