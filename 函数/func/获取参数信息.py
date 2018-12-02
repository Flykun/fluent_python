'''获取参数信息'''

from inspect import signature
from example.clip import clip

print(clip.__defaults__) # (80,)
print(clip.__code__.co_varnames)
# ('text', 'max_len', 'end', 'space_before', 'space_after')

'''可以用更好的方式 inspect'''
sig = signature(clip)
for name, param in sig.parameters.items():
    print(param.kind, ':', name, '=', param.default)
# POSITIONAL_OR_KEYWORD : text = <class 'inspect._empty'>
# POSITIONAL_OR_KEYWORD : max_len = 80
