# 通过collections模块的Iterable类型对象是否是可迭代对象
from collections.abc import Iterable

"""
    切片(Slice)：字符串，list, tuple
"""

L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
# 取前三个元素
print(L[0:3])
print(L[:3])
print(L[-1:])
print(L[-3:-1])
print(L[:])
print("__________________________________________________________________________________")

tu = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
# 取前三个元素
print(L[0:3])
print(L[:3])
print(L[-1:])
print(L[-3:-1])
print(L[:])
print("__________________________________________________________________________________")

strs = "白天黑夜交错，如此妖娆婀娜"
print(strs[0:3])
print(strs[:3])
print(strs[-1:])
print(strs[-3:-1])
print(strs[:])
print("__________________________________________________________________________________")

"""
    迭代(Iteration):
"""
d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print(key)
print("__________________________________________________________________________________")

for value in d.values():
    print(value)
print("__________________________________________________________________________________")

for item in d.items():
    print(item)
print("__________________________________________________________________________________")

# Python内置的enumerate函数可以把一个list变成索引-元素对
for i, value in enumerate(['A', 'B', 'C', 'd']):
    print(i, value)
print("__________________________________________________________________________________")

for x, y in ([1, 1], [2, 5], ['ttt', 'ssss']):
    print(x, y)
print("__________________________________________________________________________________")

print(isinstance('abc', Iterable))
print(isinstance([1, 2, 3], Iterable))
print(isinstance(123, Iterable))
print("__________________________________________________________________________________")

"""
    列表生成式：List Comprehensions，是Python内置的非常简单却强大的可以用来创建list的生成式
"""
print(list(range(1, 11)))
# 如果要生成[1x1, 2x2, 3x3, ..., 10x10]
print([x * x for x in range(1, 11)])
# 在循环后还可以加上判断语句
print([x * x for x in range(1, 11) if x % 2 == 0])
# 使用双层循环
print([m + n for m in 'ABC' for n in 'xyz'])

import os

# 通过列表生成式列出当前目录下的所有文件和文件目录
print([d for d in os.listdir(".")])

# 列表生成式使用两个变量来生成list：
d = {'x': 'A', 'y': 'B', 'z': 'C'}
print([key + "=" + value for key, value in d.items()])

# 把list中的字符串都变成小写
print([s.lower() for s in ['Hello', "World", 'IBM', "APPLe"]])
print("__________________________________________________________________________________")

"""
    生成器(generator)：通过列表生成式可以创建一个列表，但是内存是有限的，如果创建元素很多的一个列表就很占用储存空间
                      所以如果列表元素可以按照某种算法推算出来，在循环过程中不断推算出后续的元素，就不必创建完整的list。
                      一边循环一边计算的机制，节省大量的空间。
            send:与__next__()、next()同样可以让生成器继续放下执行，不同send()可以发送至给到生成器中 yide x 
"""
# 第一种方式，将列表生成式的[] 改成 ()
L = [x * x for x in range(10)]
print(L)
print(type(L))
g = (x * x for x in range(10))
print(g)
print(type(g))

# 可以通过 next()计算出g的下一个元素的值
print(next(g))
print("__________________________________________________________________________________")

# 生成器也是可迭代对象，所以可以用迭代的方式操作
for i in g:
    print(i)
print("__________________________________________________________________________________")


# 求斐波拉契数列 ，除第一个和第二个数外，任意一个数都可由前两个数相加得到
def fib(maxNum):
    n, a, b = 0, 0, 1
    while n < maxNum:
        print(b)
        a, b = b, a + b
        n = n + 1
    print('done')


fib(6)
print("__________________________________________________________________________________")


# fib函数定义了数列的推算规则，可以从第一个元素开始，推算出后面任意元素。这种逻辑十分类似生成器generator
# 如何将fib函数变成 generator.只需要将print(b)  改yield b 就可以
# 如果一个函数定义包含  yield  关键字，那么这个函数就是一个generator.而不是普通函数
def fib(maxNum):
    n, a, b = 0, 0, 1
    while n < maxNum:
        x = yield b
        print(x)
        a, b = b, a + b
        n = n + 1
    return 'done'


print(type(fib(3)))
for n in fib(5):
    print(n)
print("__________________________________________________________________________________")

# for循环调用generator时，发现拿不到generator的return语句的返回值。
# 如果想要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value中
g = fib(6)
while True:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('return value:', e.value)
        break
print("____________________________________send()______________________________________________")

# send()  将值发送给 yield 结果复制给的变量。比如此函数中 x = yied b ----> x = "传给生成器的值"
g = fib(10)
print(next(g))
print(g.__next__())
print(g.__next__())
print(g.send("传给生成器的值"))
print(g.send(None))


print("__________________________________________________________________________________")

"""
    迭代器:Iterable对象表示是一个可以进行迭代的对象，但不一定是Iterator迭代器。
          Python的Iterator对象表示的是一个数据流，是一个有序序列，但是我们却不能提前知道长度，只能通过next()计算得出，所以Iterator是惰性的
          
    小结
        凡是可作用于for循环的对象都是Iterable类型；

        凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；

        集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。

"""
from collections.abc import Iterable, Iterator

# Iterable
print(isinstance([], Iterable))
print(isinstance({}, Iterable))
print(isinstance('abc', Iterable))
print(isinstance((x for x in range(5)), Iterable))
print(isinstance(100, Iterable))
print("__________________________________________________________________________________")

# Iterator
print(isinstance([], Iterator))
print(isinstance({}, Iterator))
print(isinstance('abc', Iterator))
print(isinstance((x for x in range(5)), Iterator))
print(isinstance(100, Iterator))
print("__________________________________________________________________________________")

# iter()
print(isinstance(iter([]), Iterator))
print(isinstance(iter({}), Iterator))
print(isinstance(iter('abc'), Iterator))
print(isinstance((x for x in range(5)), Iterator))

