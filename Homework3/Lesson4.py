#4.Напишите программу, которая будет преобразовывать десятичное число в двоичное.
#
#Пример:
#
#- 45 -> 101101
#- 3 -> 11
#- 2 -> 10

start_value = int(input('Введите число для преобразования\n'))

output_bin_value = list()
value = start_value
while value > 0:
    target = value // 2
    temp = value - target * 2
    output_bin_value.append(temp)
    value = target
    if target <= 1:
        output_bin_value.append(target)
        break

output_bin_value.reverse()
output = "".join(map(str,output_bin_value))
print(f'Value = {start_value} Binary Target = {output}')