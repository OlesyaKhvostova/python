#2.Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
list_simple_value = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,
73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199,211]

def get_divide_list(input_data):
    list_value = []
    start_value = input_data
    while start_value > 1:
        if start_value == 1 or start_value in list_simple_value:
            break
        execute = False
        for i in list_simple_value:
            if start_value % i == 0:
                start_value /= i
                list_value.append(i)
                execute = True
                break

        if execute == False:
            break

    list_value.append(int(start_value))
    return list_value

input_data = int(input('Введите натуральное число\n'))
list_value = get_divide_list(input_data)
print(f'Value = {input_data} List = {list_value}')

