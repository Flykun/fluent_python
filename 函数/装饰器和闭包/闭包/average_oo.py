'''
计算移动平均值的类
'''


class Averager:
    # 计算平均值的类
    def __init__(self):
        self.series = []

    def __call__(self, new_value):
        self.series.append(new_value)
        total = sum(self.series)
        return total / len(self.series)
