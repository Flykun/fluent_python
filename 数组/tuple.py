'''
元组
'''

'''1. 元组和记录: 元组拆包'''
lax_coordinates = (33.9425, -118.408056)
city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)
traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')]
for passport in sorted(traveler_ids):
    # print(f'{passport}/{passport}')
    print('%s / %s' % passport)

for country, _ in traveler_ids:
    print(country)

latitude, longitude = lax_coordinates
print(latitude, longitude)

t = (20, 8)
print(divmod(20, 8))  # Return the tuple (x//y, x%y)
print(divmod(*t))  # * 运算符把对象拆开

# 函数用*args获取不定长参数
a, b, *rest = range(5)
print(a, b, rest)  # 0 1 [2, 3, 4]
a, b, *rest = range(2)
print(a, b, rest)  # 0 1 []
a, b, *rest, c, d = range(5)
print(a, b, rest, c, d)  # 0 1 [2] 3 4

# 嵌套元组拆包:获取经纬度
metro_areas = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
]

print('{:15} | {:^9} | {:^9}'.format('', 'lat.', 'long.'))
fmt = '{:15} | {:9.4f} | {:9.4f}'
for name, _, _, (latitude, longitude) in metro_areas:
    print(fmt.format(name, latitude, longitude))

'''具名元组'''
from collections import namedtuple

City = namedtuple('City', 'name country population coordinates')
tokyo = City('tokyo', 'JP', population=36.933,
             coordinates=(35.689722, 139.691667))
print(tokyo[2], tokyo.country)
print(City._fields)
LatLong = namedtuple('LatLong', 'lat long')
delhi_data = ('Delhi NCR', 'IN', 21.935, LatLong(28.613889, 77.208889))
delhi = City._make(delhi_data) # 同City(*delhi_data)
print(delhi._asdict())
for key, value in delhi._asdict().items():
    print(key + ': ', value)
