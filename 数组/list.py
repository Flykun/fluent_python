'''
由列表组成的列表
嵌套列表创建的正确及错误用法
'''

'''正确用法1'''
board = [['_'] * 3 for i in range(3)]
print(board)  # [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
board[1][2] = ['X']
print(board)  # [['_', '_', '_'], ['_', '_', ['X']], ['_', '_', '_']]

'''正确用法2'''
board = []
for i in range(3):
    row = ['_'] *3
    board.append(row)


'''错误用法1'''
# 三个指向同一对象的引用的列表
weird_board = [['_'] * 3] * 3
print(weird_board)  # [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
weird_board[1][2] = 'Y'
print(weird_board)  # [['_', '_', 'Y'], ['_', '_', 'Y'], ['_', '_', 'Y']]

'''错误用法2'''
row = ['_' * 3]
board = []
for i in range(3):
    board.append(i)
