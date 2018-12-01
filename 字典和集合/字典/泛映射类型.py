'''
检查是否是映射类型
'''
from collections import abc

my_dict = {}

print(isinstance(my_dict, abc.Mapping))  # True

'''字典的构造方法'''
a = dict(one=1, two=2, three=3)
b = {'one': 1, 'two': 2, 'three': 3}
c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
d = dict({'three': 3, 'two': 2, 'one': 1})

print(a == b == c == d)  # True
