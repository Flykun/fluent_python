'''函数内省:
    内部属性
    dir(函数)
'''

# 计算类没有 函数有的属性
class C: pass
obj = C()
def func(): pass

print(sorted(set(dir(func)) - set(dir(obj))))