'''高阶函数的应用'''


def factorial(n):
    '''return n'''
    return 1 if n < 2 else n * factorial(n - 1)


fact = factorial

'''以上为用于测试的函数'''

fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']
print(sorted(fruits))


def reverse(word):
    return word[::-1]


print(reverse('war'))
print(sorted(fruits, key=reverse))

'''计算阶乘, map和filter比较'''
a = list(map(fact, range(6)))
b = [fact(n) for n in range(6)]

c = list(map(fact, filter(lambda n: n % 2, range(6))))
d = [fact(n) for n in range(6) if n % 2]

print(a == b)
print(c == d)

'''使用reduce和sum计算0-99的和'''

from functools import reduce
from operator import add

print(reduce(add, range(101)))
print(sum(range(101)))