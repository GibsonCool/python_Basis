"""
    高阶函数(Higher-order function):变量可以指向函数即 函数本身可以赋值给变量。函数名字也是变量
                                   除了接收函数作为参数外，还可以把函数作为结果返回
"""
print(abs)
print(abs(-2))
x = abs
print(x)
print(x(-4))

# 函数名其实就是指向函数的变量，既然是变量也就可以指向其他值
abs = 2
print(abs)
del abs  # 删除变量abs ,解除abs对2的引用
print(abs)


def add(x, y, f):
    return f(x) + f(y)


# 将 abs 函数的函数名当做参数传入到add()函数中
print("result:", add(-5, -3, abs))


# 函数当做返回值
def lazy_sum(*args):
    """
        args 参数保存在了sum()函数中，这种称为闭包(Closure)
    """

    def sum():
        ax = 0
        for n in args:
            ax += n
        return ax

    return sum


f = lazy_sum(12, 2, 55)  # 返回的并不是求和结果，而是求和函数：
print(f)
print(f())

# 每次调用lazy_sum()都会返回一个新函数，所以即使传入相同的参数，f和f1也不相等，调用结果互不影响
f1 = lazy_sum(12, 2, 55)
print(f == f1)
print("__________________________________________________________________________________")

"""
    一些系统自带的高阶函数：map  reduce  filter sorted
"""
from collections.abc import Iterable, Iterator


def f(x):
    return x * x


"""
    map(fun,iterable):将fun函数作用于iterable上的每一个元素
"""
r = map(f, [1, 2, 3, 4, 5])
print(isinstance(r, Iterator))
print(isinstance(r, Iterable))
print(list(r))
print("__________________________________________________________________________________")

"""
    reduce(fun, iterable):将fun函数作用于iterable ,fun接受两个参数，并将结果继续和序列的下一个元素做累计计算
    reduce(fun, [x1, x2, x3, x4]) = fun(fun(fun(x1, x2), x3), x4)
"""
from functools import reduce


def add(x, y):
    return x + y


print(reduce(add, [1, 2, 3]))
print(reduce(add, [13, 2, 13, 4]))

# 将列表[1,3,5,7,9]  转换为整数13579
L = [1, 3, 5, 7, 9]


def fn(x, y):
    return x * 10 + y


print(reduce(fn, L))
print("__________________________________________________________________________________")

# 结合map reduce的一个例子，将'13579'字符串转换为数字
digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


def char2num(s):
    return digits[s]


print(reduce(fn, map(char2num, '229804')))


# 改造成一个函数
def str2int(s):
    def fn2(x, y):
        return x * 10 + y

    def char2num2(s):
        return digits[s]

    return reduce(fn2, map(char2num2, s))


print(str2int('398765'))

# 使用lambda表达式
print(reduce(lambda x, y: x * 10 + y, map(lambda n: digits[n], '23855')))
print("__________________________________________________________________________________")

"""
    filter(fun,Iterable): 和map类似，接受一个函数和一个序列，把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素 
"""

# 过滤list中的偶数，只保留奇数
l1 = [1, 2, 4, 5, 6, 9, 10, 15]
print(list(filter(lambda n: n % 2 == 1, l1)))

# 过滤空字符串
strList = ['A', '', 'B', None, 'C', '  ']

print(list(filter(lambda n: n and n.strip(), strList)))
print("__________________________________________________________________________________")

"""
    sorted(Iterable,key=fun):按照key进行排序
"""
print(sorted([36, 5, -12, 9, -21]))
# 按照绝对值大小排序
print(sorted([36, 5, -12, 9, -21], key=abs))

print(sorted(['bob', 'about', 'Zoo', 'Credit']))
# 忽律大小写排序
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))
# 将排序反向
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))
