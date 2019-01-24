"""
    ThreadLocal：一个ThreadLocal变量是全局变量(可以间接的看做一个全局的dict,key就是Thread本身 )，通过该变量获取各自线程的变量副本进行操作，互不干扰。
                ThreadLocal解决参数在一个线程中各个函数之间互相传递的问题
                常见的使用地方：为每个线程绑定一个数据库连接，HTTP请求，用户身份信息等，这样一个线程的所有调用到的处理函数都可以非常方便地访问这些资源
"""

import threading


class Student(object):
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, valueName):
        self.__name = valueName


# 创建ThreadLocal对象
localSchool = threading.local()


def process_student():
    # 取出当前线程设置的student变量
    std = localSchool.student
    print("当前线程 %s 的Student.name=> %s" % (threading.current_thread().name, std.name))


def procerss_thread(valueName):
    # 创建student并赋值给当前线程
    localSchool.student = Student(valueName)
    process_student()


t1 = threading.Thread(target=procerss_thread, args=("DoubleX",), name="Thread_牛逼")
t2 = threading.Thread(target=procerss_thread, args=("GibsonFire",), name="Thread_厉害")

t1.start()
t2.start()
t1.join()
t2.join()
