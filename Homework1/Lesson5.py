import math

a_x_value = int(input('Введите X координату точки A\n'))
a_y_value = int(input('Введите Y координату точки A\n'))
b_x_value = int(input('Введите X координату точки B\n'))
b_y_value = int(input('Введите Y координату точки B\n'))

delta_x = b_x_value - a_x_value
delta_y = b_y_value - a_y_value

distance = math.sqrt(delta_x * delta_x + delta_y * delta_y)
print(f'A({a_x_value},{a_y_value}), B({b_x_value},{b_y_value}) дистанция = {round(distance,3)}')
