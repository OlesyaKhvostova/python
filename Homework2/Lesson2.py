input_data = int(input('введите число N\n'))
list_data = list()

for i in range(1,input_data + 1):
    if i == 1:
        list_data.append(i)
    else:
        list_data.append(i * list_data[i - 2])

print(f'N = {input_data} Data = {list_data}')
