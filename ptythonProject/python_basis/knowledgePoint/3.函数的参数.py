# ------------------ 位置参数 ---------------------
# 参数x就是一个位置参数
def power(x):
    return x * x


# ------------------ 默认参数 ---------------------
# 默认参数  参数n就是一个默认参数，他的默认值就2
def power2(x, n=2):
    s = 1
    while n > 0:
        n -= 1
        s = s * x
    return s


print('------------------------------')

# 默认参数的调用 效果既可以达到power()正常调用，还可以更改默认值来扩展使用
print(power2(2))
print(power2(2, 2))
print(power2(2, 4))

print('------------------------------')


# 多个默认参数以及调用
def enroll(name, age, gender="男", city="未知"):
    print('name:', name)
    print('age:', age)
    print('gender:', gender)
    print('city:', city)
    print('------------------------------')


enroll('cxx', 20)
enroll("double", 24, "女", "深圳")
enroll('gibsonCool', 23, city='beijing')


# 默认参数的必须只想不可变对象。否则会出现以下情况
def add_end(L=[]):
    L.append("End")
    return L


print(add_end([1, 2, 3]))  # 输出正常：[1, 2, 3, 'End']
print(add_end())  # 输出正常：['End']
print(add_end([3, 4]))  # 输出正常：[3, 4, 'End']
print(add_end())  # 输出异常：['End', 'End']
print(add_end())  # 输出异常：['End', 'End', 'End']

# 这里的输出结果可以这样去理解：默认参数L = [] ,如果我们调用的时候传入了值，这L就被重新赋值了例如L = [1,2,3]
# 但是如果我们没有传参，而且默认参数就是L = [],当第一次调用后，默认参数的值就变成了L = ["End"],下次调用就是在['End']的基础上去append('End')

print('------------------------------')


# 修改上面的例子，让默认参数只想不可变对象，然后内部判断重新赋值
# 因为不变对象一旦创建，对象内部的数据就不能修改，这样就减少了由于修改数据导致的错误
def add_end_fix(L=None):
    if L is None:
        L = []
    L.append("end")
    return L


print(add_end_fix([1, 2, 3]))  # 输出正常：[1, 2, 3, 'End']
print(add_end_fix())  # 输出正常：['End']
print(add_end_fix([3, 4]))  # 输出正常：[3, 4, 'End']
print(add_end_fix())  # 输出异常：['End', 'End']
print(add_end_fix())  # 输出异常：['End', 'End', 'End']

print('------------------------------')


# ------------------ 可变参数 ---------------------
# 可变参数使用 *参数名  的形式定义。在函数内部，参数numbers接受的是一个 tuple。在调用的到时候可以传入任意个参数
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum += n * n
    return sum


print(calc(2, 3))
print(calc())
# 如果已经有一个list或tuple，要调用以个可变参数怎么处理？
nums = [1, 2, 3]
print(nums[0], nums[1], nums[2])
# 上面这种写法过于繁琐体现不出简洁,
# *nums表示把nums这个list的所有元素作为可变参数传进去。这种写法相当有用，而且很常见。
print(*nums)

print('------------------------------')


# ------------------ 关键字参数 ---------------------
# 关键字参数使用 **参数名 的形式定义。参数kw在函数内部自动封装成一个dict
def person(name, age, **kw):
    print("name:", name, "age:", age, "other", kw)


person('cxx', 23)
person('double', 24, city='beijing')
person('gibson cool', 23, gender='man', job='player')

# 和可变参数一样，关键字参数也可以组装出一个dict，然后将其转换为关键字参数穿进去
extra = {'gender': 'man', 'job': 'player', 'city': 'beijing'}

# **extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，
# kw将获得一个dict，注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra
person('GFire', 30, **extra)

print('------------------------------')


# ------------------ 命名关键字参数 ---------------------
# 为了限制关键字参数的名字，就有了命名关键字参数。限定参数名
# 命名关键字参数使用 *，参数名1，参数名2.。。  的形式定义。
def person2(name, age, *, city, job):
    print(name, age, city, job)


person2('Jack', 24, city='Beijing', job='Engineer')


# 命名关键字参数必须传入参数名，这和位置参数不同。如果没有传入参数名，调用将报错
# 由于缺少参数名city和job。Python解释器将这4个参数都视为位置参数了，明显不符合person2的函数定义
# person2('Jack宿舍', 24, 'Beijing', 'Engineer')

# 可以给命名关键字参数设置默认值，从而简化调用
def person22(name, age, *, city='beijing', job):
    print(name, age, city, job)


person22('Jack', 24, job='Engineer')


# 如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了
def person3(name, age, *args, city, job):
    print(name, age, args, city, job)


nums = [3, 4.4, 52]
person3('cxx', 33, *nums, city='beijing', job='runner')
