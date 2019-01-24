# 函数的定义 使用 'def' 定义
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x


# 函数的调用
result = my_abs(10)
print(result)

# 将函数复制给一个变量
getAbs = my_abs
result = getAbs(11)
result2 = getAbs(-22)
print(result, result2)

# 调用Python内置函数
# 求绝对值
result = abs(11)
result2 = abs(-211)
print(result, result2)

# 求最大值
print(max(1, 2, 59, -12))

''' 
    Python内置的常用函数还包括数据类型转换函数
    type() 函数可以获取值的类型
'''
print(type(int('123')))
print(int(12.32))
print(float('123.33'))
print(str(1.23))
print(str(100))
print(bool(1))
print(bool(""))
