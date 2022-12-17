#2.Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#Пример:
#- [2, 3, 4, 5, 6] => [12, 15, 16];
#- [2, 3, 5, 6] => [12, 15]
import math

data = [1,8,4,7,2,6,4,9,5,7,3]
output_data = list()

count = math.ceil(len(data) / 2)

for i in range(0,count):
    back_index = len(data) - i - 1
    output_data.append(data[i] * data[back_index])

print(f'data = {data} calc_result = {output_data}')
