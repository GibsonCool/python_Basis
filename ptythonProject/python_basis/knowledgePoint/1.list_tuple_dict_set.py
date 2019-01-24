""" list  一个可变的有序表 """
listSimple = ['a', 'b', 'c']
print(listSimple)
print(listSimple[2])
print(listSimple[-2])
# print(listSimple[3])    # 会奔溃，越界
listSimple.append("sss")
print(listSimple)
listSimple.insert(2, "555")
print(listSimple)

""" tuple  一个不可变的有序表"""
tupleSimple = (1,)  # 为了避免歧义定义只有一个元素的tuple时候需要在末尾加个逗号
print(tupleSimple)
tupleSimple

""" dict """
d = {'name': "cxx", 'age': 25, 'city': "shenzheng"}
print(d['name'])
print(d['age'])
d['age'] = 55
print(d['age'])
d['sorce'] = 100
print(d)

""" set """
setSimple = set(listSimple)
print(setSimple)
setSimple2 = set(['a', 'a', 2, 3, 4, 4])
print(setSimple2)

print(abs(-11))
