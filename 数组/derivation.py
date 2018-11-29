'''
列表推导式
列表推导式同filter和map的比较
笛卡儿积
生成器表达式
'''

'''1. 列表推导式'''
x = 'ABC'
dummy = [ord(x) for x in x]
print(x)  # ABC
print(dummy)  # ABC
# x的值被保留, 列表推导式也能创建正确的列表


'''2. 列表推导式痛filter和map的比较'''
symbols = '!@#$%^&*'
beyond_ascii = [ord(s) for s in symbols if ord(s) > 50]
print(beyond_ascii)  # [64, 94]

beyond_ascii = list(filter(lambda c: c > 50, map(ord, symbols)))
print(beyond_ascii)  # [64, 94]

'''3. 使用列表推导计算笛卡儿积'''
colors = ['block', 'white']
sizes = ['S', 'M', 'L']
t_shirts = [(color, size) for color in colors for size in sizes]
print(t_shirts)
# [('block', 'S'), ('block', 'M'), ('block', 'L'),
#  ('white', 'S'), ('white', 'M'), ('white', 'L')]

'''4. 生成器表达式'''
symbols = '!@#$%^&*'
tup = tuple(ord(symbol) for symbol in symbols)
print(tup)  # (33, 64, 35, 36, 37, 94, 38, 42)

from 数组.数组 import array

print(array('I', (ord(symbol) for symbol in symbols)))
# array('I', [33, 64, 35, 36, 37, 94, 38, 42])

colors = ['block', 'white']
sizes = ['S', 'M', 'L']
for t_shirt in (f'{c} {s}' for c in colors for s in sizes):
    print(t_shirt)
    # block S
    # block M
    # block L
    # white S
    # white M
    # white L

