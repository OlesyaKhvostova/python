input_data = int(input('введите число N\n'))
list_data = list()

for i in range(-input_data,input_data + 1):
    list_data.append(i)

index_data = input('введите индексы через пробел\n')
index_list = index_data.split(' ')
output_value = 1
for index in index_list:
    output_value *= list_data[int(index)]

print(f'Список:{list_data} Результат:{output_value}')