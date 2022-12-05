x_value = int(input('Введите X\n'))
y_value = int(input('Введите Y\n'))

quater = 0
if x_value > 0 and y_value > 0:
    quater = 1
elif x_value < 0 and y_value > 0:
    quater = 2
elif x_value < 0 and y_value < 0:
    quater = 3
elif x_value > 0 and y_value < 0:
    quater = 4

if quater:
    print(f'x = {x_value}; y = {y_value} находится в {quater} четверти')
else:
    print('Четверть не найдена')