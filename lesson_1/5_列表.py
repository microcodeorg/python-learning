"""
列表
可以改变长度的容器，以 [] 表示
"""

if __name__ == '__main__':
    # 创建列表的语法 1
    # list_0 = list()
    #
    # # 创建列表的语法 2
    list_1 = [1, 2, 3, 4, 5]
    # # 下标     0  1  2  3  4
    # print("列表: ", list_1)  # 输出 [1, 2, 3, 4, 5]
    #
    # # 获取列表元素个数
    # print("获取列表元素个数: ", len(list_1))  # 输出 5

    # # 读取元素指定下标的值
    # print("读取元素指定下标的值 list_1[0]:", list_1[0])  # 输出 1
    # print("读取元素指定下标的值 list_1[3]:", list_1[3])  # 输出 4
    #
    # # 截取其中元素
    # print("截取其中元素 list_1[1:3]: ", list_1[1:3])  # 输出 [2,3], 从下标1起, 截取到下标3，不包括下标3
    #
    # # 向列表添加元素
    # list_1.append(6)
    # print("向列表添加元素: ", list_1)  # 输出 [1, 2, 3, 4, 5, 6]
    #
    # # 删除指定元素
    # list_1.remove(1)
    # print("删除指定元素: ", list_1)  # 输出 [2, 3, 4, 5, 6]
    #
    # # 删除指定下标元素, delete
    # del list_1[0]
    # print("删除指定下标元素: del list_1[0]", list_1)  # 输出 [3, 4, 5, 6]

    # 运算
    # list_1 = [1, 2] + [3, 4]  # [1, 2, 3, 4]
    # print(list_1)
    #
    # list_2 = [1, 2] * 3
    # print(list_2)
    list_2d = []  # len(list_2d) = 0
    list_2d_0 = [1, 3]
    list_2d_1 = [3, 4]
    list_2d.append(list_2d_0)
    list_2d.append(list_2d_1)

    list_2d = [
        [1, 2],
        [3, 4]
    ]

    r = list_2d[0][0]
    print(list_2d)

