"""
字符串
"""

if __name__ == '__main__':
    # 声明字符串 "" '' """""" ''''''
    str1 = "abc"
    str2 = 'abcd'
    str3 = """
    两行
    
    """
    # print("str1 \"名字\"", str1)
    # print("str2", str2)
    # print("str3", str3)

    # 运算
    # str1 = "123" + "456"
    # print("str1", str1)
    # str2 = "123" * 3
    # print("="*50)
    pass

    # 拼接
    # xing = "李"
    # ming = "世民"
    # print("加法拼接", xing + ming)
    # print("format", "姓：{}； 名：{}".format(xing, ming))
    # shuzi3 = 3.12312
    # print(f"{shuzi3:.2f}")
    pass

    # 截取
    lishimin = "李世民"
    # print("姓：", lishimin[1])
    # print("姓：世", lishimin[2])
    # print("名：", lishimin[1:])
    pass

    # 包含
    # a = "世民"
    # print(a in lishimin)

    # 类型转换
    str1 = "123"
    str2 = "123.123"
    # print("int:", int(str1), type(int(str1)))
    # print("float:", float(str2), type(float(str2)))

    # 方法，API文档，搜索引擎
    pass
    # "a".join(['a', 'b'])
    list_1 = ['3', '1', '2', 'abc', '123']
    result = "；\n".join(list_1)  # '3 1 2 abc 123'

    """
    3; 
    1;
    2
    abc
    123
    """
    print("join", result)

