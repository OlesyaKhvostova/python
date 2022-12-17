#Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между максимальным и
# минимальным значением дробной части элементов.
#
#Пример:
#
#- [1.1, 1.2, 3.1, 10.01] => 0.19

data = [1.23, 3.45, 2.34, 3.25, 4.36, 6.75, 3.29]

max_value = data[0] - int(data[0])
min_value = max_value

for i in range(1, len(data)):
    value = data[i] - int(data[i])
    if (max_value < value):
        max_value = value
    elif (min_value > value):
        min_value = value

print(f'data = {data} delta = {max_value - min_value}')