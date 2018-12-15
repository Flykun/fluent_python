'''
迭代函数列表, 找出最大的折扣
globals函数返回一个字典, 表示当前的全局符号表
'''

from example.game_mode import *

promos = [
    globals()[name] for name in globals()
    if name.endswith('_promo')
    and name != 'best_promo'
]

def best_promo(order):
    '''选择可用的最佳折扣'''
    return max(promo(order) for promo in promos)

joe = Customer('john Doe', 0)
ann = Customer('Ann Smith', 1100)
cart = [
    LineItem('banana', 4, 0.5),
    LineItem('apple', 10, 1.5),
    LineItem('water mellon', 5, 5.0)]

