'''operator模块'''

'''计算阶乘'''
from functools import reduce


def fact1(n):
    return reduce(lambda a, b: a * b, range(1, n + 1))


'''另外一种方式'''
from operator import mul


def fact2(n):
    return reduce(mul, range(1, n + 1))

'''使用itemgetter排序元组列表'''
metro_data = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.6916677)),
    ('Delhi', 'In', 21.935, (28.613889, 71.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('Sao Paulo', 'BR', 19.649,(-23.547778, -46.635833))
]

from operator import itemgetter

for city in sorted(metro_data, key=itemgetter(1)):
    print(city)

# ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833))
# ('Delhi', 'In', 21.935, (28.613889, 71.208889))
# ('Tokyo', 'JP', 36.933, (35.689722, 139.6916677))
# ('Mexico City', 'MX', 20.142, (19.433333, -99.133333))