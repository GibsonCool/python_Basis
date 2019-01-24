"""
    由于动态语言的灵活性，可以创建一个class的实例后，再给实例绑定任何属性和方法
"""


class Student(object):
    pass


s = Student()
s.name = "kobe"  # 动态给实例绑定一个属性
print(s.name)


# 除了绑定属性外，还可以绑定方法
def set_age(self, age):
    self.age = age


from types import MethodType

s.set_age = MethodType(set_age, s)  # 给实例 s 绑定一个set_age方法
s.set_age(33)
print(s.age)

s2 = Student()


# print(s2.age) 给实例绑定的方法另一个实例不能使用，

# 为了给所有实例可以使用绑定方法，就直接给类绑定方法
def set_score(self, score):
    self.score = score


Student.set_score = set_score

s.set_score(2)
print(s.score)
s2.set_score(10)
print(s2.score)
print("__________________________________________________________________________________")

"""
    __slots__：限制能动态给class绑定的属性，但是只对当前类实例起限定作用，对集成的子类是不起作用的
"""


class StudentSlots(object):
    __slots__ = ('name', 'age', 'create_time')  # 用tuple定义允许绑定的属性名称


stuSlots = StudentSlots()
stuSlots.name = "cxx"  # 绑定属性  'name'
stuSlots.age = 40  # 绑定属性  'age'
stuSlots.create_time = "cxxx"  # 绑定属性  'create_time'


# stuSlots.city = "shenzheng"     # 绑定出错，抛出AttributeError 。因为__slots__中没有 city  这个属性


# __slots__对于继承的子类是不起作用的 ， 除非子类也定了__slots__，这样子类的实例允许自己的加上父类的__slots__


class StudentSon(StudentSlots):
    pass


class StudentSon2(StudentSlots):
    __slots__ = ('width', 'height')


stuSon = StudentSon()
stuSon.name = 'double'
stuSon.city = "shenzheng"

stuSon2 = StudentSon2()
stuSon2.name = "doubleX"
stuSon2.width = 22
# stuSon2.city = "shenzheng"   # 同样是会抛出AttributeError异常


"""
    @property:Python 内置的装饰器，负责吧一个方法变成属性调用，
            优点：我们可以对属性的赋值和获取都用方法包装起来可以进行控制，不直接暴露修。
                 然后使用@property 在将其变成属性直接调用赋值。既得到了控制又保持了简洁使用
                 
    以单下划线开头，表示是一个'保护成员' 例如 _name。
    以双下划线开头，表示是一个'私有成员' 例如 __name，只允许本省访问，子类也不行。在文本上被替换为_class__name
    
    
    @property 广泛应用到类的定义中，可以让调用者写出剪短的代码，同事保证对参数进行必要的检查
    （大部分我觉得是类型的检查，这也是弱类型语言相对强类型语言的弊端还要自己进行数据类型判断）。
    程序运行时就减少出错的可能性
"""


class StudentNormal(object):
    def get_name(self):
        return self._name

    def set_name(self, strName):
        if not isinstance(strName, str):
            raise ValueError('name must be an str')
        self._name = strName


stuNormal = StudentNormal()
stuNormal.set_name("cxx")
# stuNormal.set_name(33)         # 抛异常，出错
print(stuNormal.get_name())


class StudentProperty(object):

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, strName):
        if not isinstance(strName, str):
            raise ValueError('name must be an str')
        self._name = strName

    # 或者只定义只读属性，不定义setter方法就
    @property
    def age(self):
        return 35

    def get_score(self):
        return self.__score

    def set_score(self, value):
        self.__score = value

    # 使用此方法和@property装饰器是一样的效果
    score = property(get_score, set_score)


stuProperty = StudentProperty()
stuProperty.name = "牛逼了这个方法"
print(stuProperty.name)
# stuProperty.name = 20         # 抛异常，出错
print(stuProperty.age)
# stuProperty.age = 55         # 抛异常，出错
stuProperty.score = 99
print(stuProperty.score)

print("__________________________________________________________________________________")

"""
    多重继承、MixIn：Python 于 Java之类的语言不同的一点。Python可以多继承，就不需要多实现。但是为了区分复杂的继承关系
                   有主、辅之别便于识别，就有了MixIn "混入" 额外功能，可以理解为多继承中类似多实现的体现
                   MixIn的目的就是给一个类增加多个功能，这样，在设计类的时候，我们优先考虑通过多重继承来组合多个MixIn的功能，而不是设计多层次的复杂的继承关系
"""


class Animal(object):
    pass


# 哺乳类
class Mammal(Animal):
    pass


# 鸟类
class Bird(Animal):
    pass


# 扩展功能
class RunnableMinxIn(object):
    def run(self):
        print("running.....")


class FlyableMinXin(object):
    def fly(self):
        print("flying....")


class Dog(Mammal, RunnableMinxIn):
    pass


# 鹦鹉
class Parrot(Bird, FlyableMinXin):
    pass


class NiubiAnimal(Animal, FlyableMinXin, RunnableMinxIn):
    def run_and_fly(self):
        self.run()
        self.fly()


dog = Dog()
dog.run()
parrot = Parrot()
parrot.fly()
niubiAnimal = NiubiAnimal()
niubiAnimal.run_and_fly()

print("__________________________________________________________________________________")

"""
    定制类：系统的一些 __xx__ 函数名。是Python中的特殊方法（魔术方法），比如：
          __slots__:限制能动态给class绑定的属性，但是只对当前类实例起限定作用，对集成的子类是不起作用的
          __len__:让 class 作用域len()函数
          __str__:让 class 在print()函数中输出自己定义内容
          __repr__:效果和__str__类似，不过是返回给开发者看到的字符串
          __iter__:该方法返回一迭代对象，让class可以被用于for...in循环
          __next__:结合__iter__使用，当for循环执行就会不断调用该迭代对象的此方法拿到循环的下一个值，直到遇到StopIteration错误时退出循环
          __getitem__: 让 class 表现的想list 那样可以按照下标取出元素
          __getattr__:当调用不存在的属性时，Python解释器会试图调用此方法来常识获取属性
          __call__:让class的实例可以向函数那样子被调用
"""


class Student(object):
    def __init__(self, name):
        self.name = name


print(Student('cxx'))  # 这样直接输出的是改对象的内存地址


class StudentStr(object):
    def __init__(self, name):
        self.name = name

    # 让 class 在print()函数中输出自己定义内容
    def __str__(self):
        return "StudentStr object (name=%s)" % self.name

    # 效果和__str__类似，不过是返回给开发者看到的字符串
    __repr__ = __str__


print(StudentStr("DoubleX"))


# __next__:结合__iter__使用 实现斐波那契数列
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1  # 初始化两个计数器a,b

    def __iter__(self):
        return self  # 实例本身就是迭代对象，直接返回

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b  # 后面的值等于前两个值的和
        if self.a > 50:
            raise StopIteration()
        return self.a  # 返回下一个值


for n in Fib():
    print(n)
print("***********************")


# 让类可以像list一样通过下标访问
class FibItem(Fib):
    def __getitem__(self, item):
        self.a, self.b = 0, 1
        for x in range(item):
            value = self.__next__()
        return value


f = FibItem()
print(f[3])
print(f[4])
print(f[5])
print(f[9])


# 让类可以像list一样使用切片
class FibSlice(Fib):
    def __getitem__(self, item):
        # 如果item是索引
        if isinstance(item, int):
            self.a, self.b = 0, 1
            for x in range(item):
                value = self.__next__()
            return value

        # 如果item是切片
        if isinstance(item, slice):
            start = item.start
            stop = item.stop
            self.a, self.b = 0, 1
            L = []
            for x in range(stop):
                value = self.__next__()
                if x >= start:
                    L.append(value)
            return L


f = FibSlice()
print(f[1:4])
print(f[2:9])
print("***********************")


# 如果调用不存在的属性
class StudentAttr(object):
    def __init__(self):
        self.name = "Michael"

    def __getattr__(self, item):
        if item == 'age':
            return 23
        if item == 'get_score':
            return lambda: 99
        if item == 'get_width':
            return 'this function is already exists,so can not called!'

        # 如果不定义错误处理，默认都是返回None
        # raise AttributeError('Student object has no attribute  %s ' % item)

    def get_width(self):
        return 44


stuAttr = StudentAttr()
print(stuAttr.name)
print(stuAttr.age)
print(stuAttr.get_score)
print(stuAttr.get_score())
print(stuAttr.get_width())
print(stuAttr.abc)

print("***********************")


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
print("__________________________________________________________________________________")
"""
    枚举类(Enum)：枚举类定义一个class类型。然后每个常量都是class的一个唯一实例
                 value属性则是自动赋给成员的int常量，默认从1开始计数。
    
"""

from enum import Enum

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
for name, member in Month.__members__.items():
    print(name, '=》', member, ',', member.value)
# 继承Enum自定义类，更精确的控制枚举类型
from enum import Enum, unique


# @unique 装饰器可以帮助我们检查保证没有重复值
@unique
class WeekDay(Enum):
    Sun = 0  # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6


print("***********************")
# 枚举类的访问
print(WeekDay.Sun)
print(WeekDay['Tue'])
print(WeekDay.Tue.value)
day1 = WeekDay.Tue
print(WeekDay.Tue == day1)
print(WeekDay(3))
# 访问不存在的value 或者 name会出错
# print(WeekDay(7))
# print(WeekDay['cxx'])

print("__________________________________________________________________________________")
"""
    动态语言和静态语言的最大不同，就是在函数和类的定义，不是编译时定义的，而是运行时动态创建的
    type(): 可以查看一个类型或变量的类型
            既可以返回一个对象的类型，还可以创建出新的类型
"""


class Hello(object):
    """
        test 文档注释内容
    """
    def hello(self, name='world'):
        print('Hello, %s' % name)


h = Hello()
print(type(Hello))
print(type(h))


# type(类名,继承的父类集合,要绑定的函数与函数名)
def fn(self, name='world'):  # 先定义好函数
    print('Hello, %s' % name)


def fn1(self, name='DoubleX'):
    print('%s is running.....' % name)


People = type('People', (object,), dict(hello=fn, running=fn1, name="cxx"))  # 创建Peo ple class
xiaohong = People()
xiaohong.hello()
xiaohong.running()
print(xiaohong.name)
print(help(Hello))
