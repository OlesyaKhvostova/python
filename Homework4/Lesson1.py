from decimal import Decimal
import math

def get_order(input_value):
    order = 0
    while input_value < 1:
        order += 1
        input_value *= 10
    return order

input_data = Decimal(float(input('Введите точность числа П\n')))
print(round(math.pi, get_order(input_data)))