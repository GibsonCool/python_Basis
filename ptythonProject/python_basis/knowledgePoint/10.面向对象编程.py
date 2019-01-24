"""
    Python定义类，通过 "class" 关键字
"""


# 类和实例，类的方法，封装
# class后面紧接着是类名，即Student，类名通常是大写开头的单词，紧接着是(object)，
# 表示该类是从哪个类继承下来的，继承的概念我们后面再讲，通常，如果没有合适的继承类，就使用object类，这是所有类最终都会继承的类
class Student(object):

    # __init__ 类创建的初始化方法。第一个参数永远是self表示Student实例本身。
    # 然后把name,score属性绑定到self上
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print("%s : %s " % (self.name, self.score))


bar = Student('cxx', 24)
print(bar.name)
bar.print_score()
print("__________________________________________________________________________________")

"""
    访问限制：在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问
"""


class Student2(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print("%s : %s " % (self.__name, self.__score))

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_name(self, strName):
        self.__name = strName

    def set_score(self, intScore):
        # 通过私用属性，并自己提空访问和修改的方式，可以自我控制比如传入值是否符合规范
        if 0 <= intScore <= 100:
            self.__score = intScore
        else:
            raise ValueError("传入的值必须在0~100之间")


bar2 = Student2('doublex', 22)
# 下面访问就会报错 AttributeError: 'Student2' object has no attribute 'name'
# print(bar2.name)
# print(bar2.__name)


# 通过内部提供的 get_name 和 get_score 访问
print(bar2.get_name())
print(bar2.get_score())

# 通过内部提供的 set_name 和 set_score 对属性进行修改
bar2.set_name("gibsoncool")
bar2.set_score(33)

"""
    不能直接访问__name是因为Python解释器对外把__name变量改成了_Student__name或者其他命名，这个跟Python解释器不同有关
    
    下面的做法是错误的，并不是给__name赋值，而是给bar2增加了一个__name的变量，和内部被Python解释器改名过的"__name"不是同一个
"""
bar2.__name = '6666'
print(bar2.__name)
print(bar2.get_name())  # 可以看到真正的__name并没有改变

# 通过dir()函数可以查看该对象所有属性和方法。可以看到私有变量被改了命名的信息
print(dir(bar2))
print(bar2._Student2__name)

print("__________________________________________________________________________________")

"""
    继承和多态(面向对象思想都一样，和Java差不多)：
"""


class Animal(object):
    def run(self):
        print("Animal is running ......")

    def eat(self):
        print("eat something...")


class Dog(Animal):
    def run(self):
        print("Dog is running....")


class Cat(Animal):
    def run(self):
        print("Cat is running....")


animal = Animal()
animal.run()
animal.eat()

dog = Dog()
dog.run()
dog.eat()

cat = Cat()
cat.run()
cat.eat()
print("__________________________________________________________________________________")

"""
    对于静态语言（例如Java）来说，如果需要传入Animal类型，则传入的对象必须是Animal类型或者它的子类，否则，将无法调用run()方法。
    对于Python这样的动态语言来说，则不一定需要传入Animal类型。我们只需要保证传入的对象有一个run()方法就可以了
"""


def run_func(animal):
    animal.run()


run_func(animal)
run_func(dog)
run_func(cat)


class Nothing(object):
    def run(self):
        print("我没有继承Animal，我也可以一样跑")


nothing = Nothing()
run_func(nothing)
print("__________________________________________________________________________________")

"""
    实例属性和类属性：直接在class中定义的属性是类属性，归该类所有。如果实例属性和类属性重名。实例属性高于类属性
"""


class Student3(object):
    name = 'student'


s = Student3()
print(s.name)  # 打印name属性，因为实例并没有name属性，所以会继续查找class的name属性
print(Student3.name)  # 打印类的name属性
s.name = 'Michael'  # 给实例绑定name属性
s.name = 'Michael'  # 给实例绑定name属性
print(s.name)  # 由于实例属性优先级比类属性高，因此，它会屏蔽掉类的name属性
print(Student3.name)  # 但是类属性并未消失，用Student.name仍然可以访问
del s.name  # 如果删除实例的name属性
print(s.name)  # 再次调用s.name，由于实例的name属性没有找到，类的name属性就显示出来了
