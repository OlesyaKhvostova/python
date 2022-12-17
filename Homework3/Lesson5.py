#5.Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
#
#Пример:

#- для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

step_value = int(input('Введите число\n'))

fibonachi_list = [0]
fibonachi_target_list = []

for i in range(0,step_value):
    len_list = len(fibonachi_list)
    if (len_list == 1):
        fibonachi_list.append(1)
        fibonachi_target_list.append(1)
    else:
        fibonachi_list.append(fibonachi_list[len_list - 1] + fibonachi_list[len_list - 2])
        fibonachi_target_list.append(fibonachi_list[len_list] * (-1 if i % 2 else 1))

fibonachi_target_list.reverse()
fibonachi_target_list.extend(fibonachi_list)

print(f'Value = {step_value} Result = {fibonachi_target_list}')
