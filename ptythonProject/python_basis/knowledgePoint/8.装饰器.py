"""
    装饰器(Decorator):在Python中的一种无侵入式的语法糖（有点类似AOP面向切面编程的思想），对已经存在的函数的功能进行增强
                    导入functools模块，使用@functools.wraps(func)可以消除装饰器带来的副作用。比如函数名被装饰器替换，文档注释被覆盖
"""
import time


def now():
    print(time.time())


f = now
f()

# 函数对象有一个__name__属性，可以拿到函数的名字
print(now.__name__)
print(f.__name__)
print("__________________________________________________________________________________")


# 需要在now()函数上增加一个打印日志的功能，但是又不去改动now()函数的定义
def log(func):
    def wrapper(*args, **kw):
        print("call %s()" % func.__name__)
        return func(*args, **kw)

    return wrapper


# 借助Python语法糖 @
@log  # 这里相当于执行了  now2 = log(now)
def now2():
    print(time.time())
    return "result"


print(now2())


# 如果生成器本身需要传入参数
def log2(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print("%s call %s()" % (text, func.__name__))
            return func(*args, **kw)

        return wrapper

    return decorator


@log2('cxx')  # 相当于 now3 = log2('cxx')(now3)
def now3():
    print(time.time())
    return "test"


print(now3())
print("__________________________________________________________________________________")

# 上面的方式已经实现了无侵入，加Log了，但是一开始提到了函数都有个__name__属性
# 可以从结果看出 now2  now3 经过装饰器之后名称都变了】
print(now.__name__)  # ---> now
print(now2.__name__)  # ---> wrapper
print(now3.__name__)  # ---> wrapper
print("__________________________________________________________________________________")

# 因为返回的那个wrapper()函数名字就是'wrapper'，所以，需要把原始函数的__name__等属性复制到wrapper()函数中，
# 否则，有些依赖函数签名的代码执行就会出错。不需要编写wrapper.__name__ = func.__name__这样的代码，
# Python内置的functools.wraps就是干这个事的，

import functools


def logfix(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print("call %s()" % func.__name__)
        return func(*args, **kw)

    return wrapper


def log2fix(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print("%s call %s()" % (text, func.__name__))
            return func(*args, **kw)

        return wrapper

    return decorator


@logfix
def now4():
    print(time.time())
    return "result"


@log2fix('cxx')
def now5():
    print(time.time())
    return "test"


print(now4.__name__)  # ---> now4
print(now5.__name__)  # ---> now5
print('_' * 80)


# 多个装饰器
def makeBold(func):
    print("----a----")

    @functools.wraps(func)
    def wrapper(*args, **kw):
        print("----1----")
        return "<b>" + func(*args, **kw) + "</b>"

    return wrapper


def makeItalic(func):
    print("----b----")

    @functools.wraps(func)
    def wrapper(*args, **kw):
        print("----2----")
        return "<li>" + func(*args, **kw) + "</li>"

    return wrapper


# 相当于 now6 = makeBold(makeItalic(now6()))
# 多个装饰器的时候，从输出结果可以看出，从下往上进行装饰(Python解释器解析到的时候就开始进行装饰了)，调用却是把装饰结果从上往下调用（真正调用的时候）,
@makeBold
@makeItalic
def now6():
    print("----3----")
    return "hello world now6"


print(now6())
