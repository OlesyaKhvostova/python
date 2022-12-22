#1.Вычислить число c заданной точностью d
#
#Пример:
#
#- при d = 0.001, π = 3.141
#Ввод: 0.01
#    Вывод: 3.14
#
#    Ввод: 0.001
#    Вывод: 3.141

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