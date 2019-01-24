"""
    协程（又称微线程，纤程。英文名Coroutine）:Python通过生成器的关键字"yield"实现，
                                    协程相对于进程和线程的最大区别是其切换和调动不在是受操作系统调度算法控制，可以自行控制

"""
import time


def A():
    while True:
        print('------A-----')
        yield
        time.sleep(0.5)


def B(c):
    while True:
        print('------B-----')
        next(c)
        time.sleep(0.5)


a = A()
# B(a)


"""
    需要自行安装greenlet库
    greenlet:是Python的一个C扩展，提供可自行调度的"微线程"
"""
from greenlet import greenlet


def test1():
    while True:
        print('------test1-----')
        gr2.switch()
        time.sleep(0.5)


def test2():
    while True:
        print('------test2-----')
        gr1.switch()
        time.sleep(0.5)


gr1 = greenlet(test1)
gr2 = greenlet(test2)
# gr1.switch()

"""
    需要自行安装gevent库
    gevent:基于greenlet库实现的网络并发框架，可以实现遇到耗时操作时自动进行切换
"""
import gevent


def f(n):
    for i in range(n):
        print("协程名称：%s,  value = %s" % (gevent.getcurrent(), i))
        # 如果这里没有延时耗时操作，gevent就不会切换直到执行完在切换到后面一个去
        gevent.sleep(1)


ge1 = gevent.spawn(f, 5)
ge2 = gevent.spawn(f, 5)
ge3 = gevent.spawn(f, 5)
ge1.join()
ge2.join()
ge3.join()
