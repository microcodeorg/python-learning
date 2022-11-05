"""
类，对象的模板
关键字 Class
"""
from dataclasses import dataclass


class People:
    # 类的属性 (公有，私有), public/protected/private
    name = "公有类属性"
    _name = '保护类属性'
    __name = '私有类属性'

    # 构造函数
    def __init__(self, firstname):
        self.firstname = firstname
        self.last_name = "abc"
        # 实例的属性 (公有，私有)
        self.age = "公有实例属性"
        self._age = '保护实例属性'
        self.__age = 0

    # 类的方法
    def hello(self, lastname):
        print("调用hello", self.firstname, lastname)

    # get set
    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age < 1 or age > 200:
            return

        print("调用了set_my_name")
        self.__age = age

    # 静态方法
    @staticmethod
    def static_call():
        print("调用静态方法")

    # 类方法
    @classmethod
    def class_call(cls):
        print("调用静态方法", cls.name)

    # 魔术方法
    def __str__(self):
        print("""
        People(id)
        """)


print("People 类属性:", People.name)


# 继承
class Student(People):

    def __init__(self, firstname):
        super().__init__(firstname)

    def study(self):
        print("study")


# dataclass
@dataclass
class Box:
    id: int
    name: str


if __name__ == '__main__':
    # 实例         类
    zhang_san = People("zhang_san")
    zhang_san.hello("lastname")

    fn = zhang_san.firstname
    print("张三 age:", zhang_san.age)

    zhang_san.age = 9

    print(People.static_call())
    print(People.class_call())

    print(f"{zhang_san}")

    li_si = Student(firstname="li si")
    li_si.hello("lastname")
    li_si.study()

    box1 = Box(id=1, name="box1")

# print(People.name)
# print(People.last_name)  # 错误
