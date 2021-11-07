from abc import ABC, abstractmethod

class Clothes(ABC):
    def __init__(self,type : str):
        self.type = type

    @abstractmethod
    def calc_sqr(self):
        pass


class Coat(Clothes):
    def __init__(self, size_v : float):
        super().__init__('coat')
        self.size_v = size_v

    def calc_sqr(self):
        return (self.size_v/6.5 + 0.5)

    @property
    def sqrt(self):
        return self.calc_sqr()


class Suit(Clothes):
    def __init__(self, size_h : float):
        super().__init__('suit')
        self.size_h = size_h

    def calc_sqr(self):
        return (2 * self.size_h + 0.3)

    @property
    def sqrt(self):
        return self.calc_sqr()



suit = Suit(2.0)
coat = Coat(4.0)

print(f'suit sqr = {suit.calc_sqr()} and coat sqr = {coat.calc_sqr()}')
print(f'suit sqr = {suit.sqrt} and coat sqr = {coat.sqrt}')

list_h = [h * 0.1 for h in range(10, 100, 5)]
print(*list_h)
list_suit = [Suit(val) for val in list_h]

val = ''
sqrt_val = 0.0
for _ in list_suit:
    sqrt_val += _.sqrt
    val += f'suit sqr = {_.sqrt};'

print(val)
print(f'Full sqrt = {sqrt_val}')

