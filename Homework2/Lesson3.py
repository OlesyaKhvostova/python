input_data = int(input('введите число N\n'))
list_data = list()

summ = 0
for i in range(1,input_data + 1):
    calc_value =  (1 + 1/i) ** i
    summ += calc_value
    list_data.append(calc_value)

output = ""
for val in list_data:
    output += f'{val:0.2f},'

print(f'N = {input_data} Data = {output} Summ = {summ:0.2f}')