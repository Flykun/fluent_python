'''反汇编'''

from dis import dis

print(dis('{1}'))

'''构造方法, 不可变集合'''
frozenset(range(10))