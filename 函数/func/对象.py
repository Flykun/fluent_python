'''把函数视为对象'''

# 建立测试函数


def factorial(n):
    '''return n'''
    return 1 if n < 2 else n * factorial(n - 1)

print(factorial(4))
print(factorial.__doc__)
print(type(factorial))

# 别名
fact = factorial
print(fact(5))

print(list(map(fact, range(11))))
# [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800]
