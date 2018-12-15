'''
实现Order类, 支持插入式折扣策略
在实例化订单以前, 系统会以某种方式选择一种促销折扣策略
'''

from abc import ABC, abstractmethod
from collections import namedtuple

Customer = namedtuple('Customer', 'name fidelity')


class LineItem:
    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price

    def total(self):
        return self.price * self.quantity


class Order:
    def __init__(self, customer, cart, promotion):
        self.customer = customer
        self.cart = list(cart)
        self.promotion = promotion

    def total(self):
        if not hasattr(self, '__total'):
            self.__total = sum(item.total() for item in self.cart)
        return self.__total

    def due(self):
        if self.promotion is None:
            discount = 0
        else:
            discount = self.promotion.discount(self)
        return self.total() - discount

    def __repr__(self):
        fmt = '<Order total: {:.2f} due: {:.2f}>'
        return fmt.format(self.total(), self.due())


class Promotion(ABC):
    # 策略: 抽象基类
    @abstractmethod
    def discount(self, order):
        '''返回折扣金额(正值)'''


class FidelityPromo(Promotion):
    '''积分为1000或以上的顾客提供5%的折扣'''

    def discount(self, order):
        return order.total() * 0.05 if order.customer.fidelity >= 1000 else 0


class BulkItemPromo(Promotion):
    '''单个商品为20个或以上时提供10%折扣'''

    def discount(self, order):
        discount = 0
        for item in order.cart:
            if item.quantity >= 20:
                discount += item.total * 0.1
        return discount


class LargeOrderPromo(Promotion):
    '''订单中的不同商品达到10个或以上时提供7%的折扣'''

    def discount(self, order):
        discount_items = {item.product for item in order.cart}
        if len(discount_items) >= 10:
            return order.total() * 0.07
        return 0


if __name__ == '__main__':
    joe = Customer('john Doe', 0)
    ann = Customer('Ann Smith', 1100)
    cart = [
        LineItem('banana', 4, 0.5),
        LineItem('apple', 10, 1.5),
        LineItem('water mellon', 5, 5.0)
    ]
    print(Order(ann, cart, FidelityPromo()))
    print(Order(joe, cart, FidelityPromo()))