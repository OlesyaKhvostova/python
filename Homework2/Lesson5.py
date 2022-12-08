import random

input_data = int(input('введите число N\n'))
list_data = list()

for i in range(0, input_data + 1):
    list_data.append(i)
print(f'Original List:{list_data}')

for i in range(0, len(list_data)):
    first_index = random.randint(0,len(list_data) - 1)
    second_index = random.randint(0,len(list_data) - 1)

    if (second_index == first_index):
        second_index = random.randint(0,len(list_data) - 1)

    temp = list_data[first_index]
    list_data[first_index] = list_data[second_index]
    list_data[second_index] = temp


print(f'Mixed List:{list_data}')