'''
基本类型传参-值传参-传递堆地址-不影响外界
对象传参-引用传参-传递栈地址-会影响外界
内存与堆栈原理示意图请见temp下【内存原理示意图.png】
'''


name = "zhangsan"


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p = Person(name, 20)


# 基本类型传参，传递的是【值（堆地址）】
# 由于函数传参传递的是【值（堆地址）】而非【引用（栈地址）】，所以函数对name的修改，在外界不起作用
def changeName(name):
    name = "lisi"


# 对象传参传递的是【引用（栈地址）】
# 因此函数内修改，函数外依然起作用
def changePerson(p):
    p.name = "fuck"


if __name__ == '__main__':

    changeName(name)
    print(name)

    changePerson(p)
    print(p.name)
