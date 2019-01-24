"""
    类装饰器：利用__call__是类的实例可以像方法一样被调用。

"""


# 让类的实例直接调用，像方法一样调用
class StudentCall(object):
    def __init__(self, name):
        self.name = name

    def __call__(self, *args, **kwargs):
        print("My name is %s" % self.name)


studentCall = StudentCall("刘德华")
studentCall()
# 通过 callable()函数可以判断一个对象是否是"可调用"对象
print(callable(max))
print(callable([1, 2, 3]))
print(callable(studentCall))
print("*" * 80)


class Test(object):
    def __init__(self, func):
        self.name = "cxx"
        print("__初始化__")
        print("func name is %s " % func.__name__)
        self.__func = func

    def __call__(self, *args, **kwargs):
        print("____装饰器中的功能____")
        self.__func()


"""
    相当于 testFun = Test(testFun)  创建了一个Test()对象，并传入了testFun函数，并把这个对象最后赋值给testFun
    最终testFun() 就相当于调用对象的__call__方法
"""

@Test
def testFun():
    print("---test  func---")


testFun()
print(testFun.name)
