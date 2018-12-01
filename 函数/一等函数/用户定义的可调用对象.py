import random


class BingoCage():
    def __init__(self, items):
        self._items = list(items)
        random.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from empty BingoCage')

    def show(self):
        return self._items

    def __call__(self, *args, **kwargs):
        return self.pick()

if __name__ == '__main__':
    bingo = BingoCage(range(5))
    print(bingo.show())
    print(bingo.pick())
    print(bingo.show())
    print(bingo()) # 回到pick()
