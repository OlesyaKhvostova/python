#3.Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
#Ввод: [1, 1, 2, 3, 4, 4, 4]
#Вывод: [2, 3]

list_data = [1, 1, 2, 3, 4, 4, 4, 7, 5,5,9]
list_result = []
for i in range(len(list_data)):
    if not (list_data[i] in list_data[i + 1:] or list_data[i] in list_data[:i]):
        list_result.append(list_data[i])

print(f'Original {list_data}\n')
print(f'Result {list_result}\n')
