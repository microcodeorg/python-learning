"""
函数
关键字 def
作用: 封装代码, 重用
蛇形命名法，全小写
"""


# 声明函数
def some_useful_function():
    """
    无参函数
    defind
    """
    print("is_func: 这是一段很复杂的代码")


# 调用函数
some_useful_function()
some_useful_function()


def is_func2(arg_1, arg_2):
    """
    位置参数
    """
    print("参数:", arg_1, arg_2)


print("is_func2")
is_func2(10, 123)


def is_func3(arg_1, arg_2=100):
    """
    默认参数
    必须声明在普通参数后面
    """
    print("默认参数:", arg_1, arg_2)


is_func3(10)


def is_func4(arg_1, arg_2, *args):
    """
    可变长参数
    """
    print("可变长参数:", arg_1, arg_2, *args)
    print("args", type(args))


is_func4(50, 60, 10, 20, 10, 30, 123, "asdf")


def is_func5(arg_1, arg_2="abc", arg_3=10, arg_4=10, arg_5=10, arg_6=10, **kwargs):
    """
    关键字参数,
    作用: 参数很多的时候
    """
    print("关键字参数:", arg_1, arg_2, arg_3, arg_4, arg_5, arg_6, kwargs, kwargs['apple'])


is_func5(arg_1=10, arg_2="", arg_3=30, apple=1)


# 返回值
def is_func6(num_1, num_2):
    """
    返回值
    """
    return num_1 + num_2


print("返回值:", is_func6(10, 20))


# 返回值
def return_two_value(num_1, num_2):
    """
    返回值
    """
    return num_1 + num_2, num_1 * num_2


val_1, val_2 = return_two_value(10, 20)
print("返回值:", val_1, val_2)

# 变量的作用域。
is_global_val = 10  # 全局变量


def func7():
    global is_global_val
    print("is_global_val:", is_global_val)
    # is_global_val = 20  # 不能直接修改全局变量

    is_global_val = 20


func7()


def func_8(cb):
    """
    lambda表达式
    """

    print("add:", cb(10, 20))


func_8(lambda x, y: x + y)


def func_9():
    """
    函数里面声明函数
    """

    def func_10():
        print("call func_10")

        def func_11():
            print("call func_11")

        func_11()

    func_10()


func_9()
