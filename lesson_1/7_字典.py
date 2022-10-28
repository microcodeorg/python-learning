"""
字典
字典当中的元素是通过键来存取的
以 {} 表示
"""

if __name__ == '__main__':
    # 创建字典的语法
    # list1 = ["张飞", "关羽", "刘备"]
    #
    # guanyu = list1[1]

    # key, value
    lgz = dict(关羽="关羽值", 张飞="张飞值", 刘备="刘备值")

    dict_1 = lgz
    # print("字典: ", dict_1)
    # print("关羽的值", lgz["关羽"])
    # print("="*20)
    # dict_1['关羽'] = "关羽22"
    # print("关羽的值", lgz["关羽"])
    # print("字典: ", dict_1)
    #
    # 获取字典元素个数
    print("获取字典元素个数: ", len(dict_1))
    #

    # 读取元素指定键值的值
    # print("读取元素指定键值的值: dict_1['a']=", dict_1['张飞'])
    #

    # 添加元素指定键值的值
    # dict_1["曹操"] = "曹操值"
    # print("添加元素指定键值的值: ", dict_1)
    #
    # 删除元素指定键值的值
    del dict_1["刘备"]
    print("删除元素指定键值的值: ", dict_1)

    # # 输出所有 Key
    # print(dict_1.keys())
    # # 输出所有 值
    # print(dict_1.values())

    dict_1['dict2'] = dict(我是dict2="2")
    print(dict_1)
