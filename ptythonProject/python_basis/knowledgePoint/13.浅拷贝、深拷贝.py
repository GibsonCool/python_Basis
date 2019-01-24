"""
    ==：比较的是值
    is：比较的是地址值

"""

a = [11, 22, 33]
b = [11, 22, 33]
print(id(a))
print(id(b))
print(a == b)
print(a is b)

print("__________________________________________________________________________________")

"""
    浅拷贝(copy.copy())：正常的赋值操作，只拷贝地址值或者叫内存引用，如果有多层只拷贝第一层，如果第一层是不可变比如元组，那么一层都不拷贝直接复制
    深拷贝(copy.deepcopy())：直接拷贝值(地址值指向的内容)
"""
c = a
print(id(c))
print(c == a)
print(c is a)

import copy

d = copy.deepcopy(a)
print(id(d))
print(d == a)
print(d is a)
print("~~~~~~~~~~~~~~~~~~~~~~~~~")

c = [a, b]
print(id(c))
print(c)

e = copy.copy(c)
print(id(e))
print(e)
a.append(99)
print(c)
print(e)
print("~~~~~~~~~~~~~~~~~~~~~~~~~")

c = (a, b)
print(id(c))
print(c)

e = copy.copy(c)
print(id(e))
print(e)
a.append(99)
print(c)
print(e)
