import copy
from decimal import Decimal
prices = [57.8, 46.51, 97, 10.12, 30, 90.34, 115.5, 56.34, 23, 34.87, 98, 132.23, 156.23, 876.3]

def print_prices(prices):
    price_output = ''
    for price in prices:
        rubles = int(price)
        data = Decimal.from_float(price) * 100
        rubl_part = int(data.to_integral()) - rubles * 100
        price_output += f'{rubles} руб {rubl_part:02d} коп'
        if (price != prices[-1]):
            price_output += ', '
    return price_output
#Пункт А
print(print_prices(prices))
#Пункт В
print(id(prices))
prices.sort()
print(print_prices(prices))
print(id(prices))
#Пункт С
prices_sort = copy.copy(prices)
print(id(prices_sort))
prices_sort.sort(reverse=True)
print(print_prices(prices_sort))
#Пункт D
print(print_prices(prices_sort[4::-1]))



