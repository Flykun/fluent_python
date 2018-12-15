'''
装饰器的一个关键特性是函数定义以后立刻运行
'''

registry = []


def register(func):
    print('running register(%s)' % func)
    registry.append(func)
    return func


@register
def f1():
    print('run f1()')


@register
def f2():
    print('run f2()')


def f3():
    print('run f3()')


def main():
    print('running main()')
    print('registry -> ', registry)
    f1()
    f2()
    f3()


if __name__ == "__main__":
    main()
