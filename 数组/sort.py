'''
sorted方法与排序
'''
'''1. sorted方法'''
fruits = ['grape', 'respberry', 'apple', 'banana']
print(fruits)  # ['grape', 'respberry', 'apple', 'banana']
print(sorted(fruits))  # ['apple', 'banana', 'grape', 'respberry']
# ['respberry', 'grape', 'banana', 'apple']
print(sorted(fruits, reverse=True))
print(sorted(fruits, key=len))  # ['grape', 'apple', 'banana', 'respberry']

'''2. bisect排序'''
import bisect
import sys

haystack = [1, 4, 5, 6, 8, 12, 15, 20, 21, 23, 23, 26, 29, 30]
needles = [0, 1, 2, 5, 8, 10, 22, 23, 29, 30, 31]
row_fmt = '{0:2d}@{1:2d}    {2}{0:<2d}'


def demo(bisect_fn):
    for needle in reversed(needles):
        position = bisect_fn(haystack, needle)
        offset = position * '  |'
        print(row_fmt.format(needle, position, offset))

if __name__ == '__main__':
    if sys.argv[-1] == 'left':
        bisect_fn = bisect.bisect_left
    else:
        bisect_fn = bisect.bisect

    print('demo: ', bisect_fn.__name__)
    print('haystack -> ', ''.join('%s' % n for n in haystack))
    demo(bisect_fn)
'''
demo:  bisect
haystack ->  14568121520212323262930
31@14      |  |  |  |  |  |  |  |  |  |  |  |  |  |31
30@14      |  |  |  |  |  |  |  |  |  |  |  |  |  |30
29@13      |  |  |  |  |  |  |  |  |  |  |  |  |29
23@11      |  |  |  |  |  |  |  |  |  |  |23
22@ 9      |  |  |  |  |  |  |  |  |22
10@ 5      |  |  |  |  |10
 8@ 5      |  |  |  |  |8 
 5@ 3      |  |  |5 
 2@ 1      |2 
 1@ 1      |1 
 0@ 0    0 
'''