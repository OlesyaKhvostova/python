#4.Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
#
#Пример:
#
#- k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
#- k=4 => 8*(x**4) + 9*(x**3) + 1*(x**2) + 5*x + 4 = 0 или 8*(x**4) + 5*x + 4 = 0 и т.д.
import random

def generate_data(order):
    list_data = []
    for i in range(order,-1,-1):
        value = random.randint(0,101)
        if i > 0:
            str_value = f'{value}*(X**{i})'
        else:
            str_value = f'{value}'

        list_data.append(str_value)

    return ' + '.join(list_data)

order = int(input('Ведите порядок многочлена\n'))
result_first = generate_data(order) + ' = 0'
result_second = generate_data(order) + ' = 0'

print(result_first, '\n')
print(result_second)

file_first = open('task1.txt','w+')
try:
    file_first.write(result_first)
finally:
    file_first.close()


file_second = open('task2.txt','w+')
try:
    file_second.write(result_first)
finally:
    file_second.close()

