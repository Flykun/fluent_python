def deco(func):
    def inner():
        print('运行 inner()')
    return inner

@deco
def target():
    print('运行 target()')

target()
print(target)