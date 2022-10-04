"""
列表、字典 列表生成式
"""

if __name__ == '__main__':
    # range(start,stop[,step]), python内置函数, 用于生成一系列连续的整数
    print(range(10))

    # range, 从0至10，每间隔3个取一个数
    L = range(0, 10, 3)
    print("从0至10, 每间隔3个取一个数: ", list(L))

    #########列表生成器###########

    # 简单的列表生成式, 生成 0 至 9 数组列表
    L = [x for x in range(10)] #等价于 #list(L)
    print("生成 0 至 9 数组列表: ", L)

    # 对产生的数据进行 * 2 操作
    L = [x * 2 for x in range(10)]
    print("对列表的数据进行 * 2 操作: ", L)

    # 将一个list中所有的字符串变成小写
    words = ["Hello", "World", "GOOD"]
    L = [w.lower() for w in words]
    print("将一个list中所有的字符串变成小写: ", L)

    # 对列表进行筛选, 只留下偶数
    L = [x for x in range(10) if x % 2 == 0]
    print("对列表进行筛选, 只留下偶数: ", L)

    # 列表可使用多层循环，如下(两层):
    L = [m + '-' + n for m in 'ABC' for n in 'XYZ']
    print("列表两层循环: ", L)

    #########字典生成器###########
    """字典生成器和列表生成器类似, 只需将 [] 换成 {}"""
    
    # 生成字典, 将 x 作为键, x * 2作为值
    D = { x: x * 2 for x in range(10) }
    print("将 x 作为键, x * 2作为值: ", D)

    # 字典生成器筛选, 只留下偶数
    D = { x: x * 2 for x in range(10) if x % 2 == 0}
    print("字典生成器筛选, 只留下偶数: ", D)