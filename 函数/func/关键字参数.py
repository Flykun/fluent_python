'''从定位参数到仅限关键字参数'''


def tag(name, *content, cls=None, **attrs):
    '''生成一个或多个HTML标签'''
    if cls is not None:
        attrs['class'] = cls
    if attrs:
        attr_str = ''.join(f'{attr}={value}'
                           for attr, value in sorted(attrs.items()))
    else:
        attr_str = ''
    if content:
        return '\n'.join(f'<{name} {attr_str}>{c}</{name}>' for c in content)
    else:
        return f'<{name}{attr_str} />'


print(tag('br'))  # <br />
print(tag('p', 'hello'))  # <p>hello</p>
print(tag('p', 'hello', 'world'))
print(tag('p', 'hello', id=3))