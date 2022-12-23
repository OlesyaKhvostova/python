#5.Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов (складываются числа, у которых "х" в одинаковых степенях). Пример того, что будет в итогвом файле: 8*(x**4) + 9*(x**3) + 1*(x**2) + 5*x + 4 = 0

def get_data_from_file(file_name:str):
    file_open = open(file_name,'r')
    data = ''
    try:
        data = file_open.readline()
    finally:
        file_open.close()

    return data

def write_data_to_file(file_name, data:str):
    file_first = open(file_name,'w+')
    try:
        file_first.write(data)
    finally:
        file_first.close()

def get_data_map(data:str):
    data_map = {}
    end_pos = data.find(' = 0')
    list_data = data[0:end_pos].split(' + ')
    for val in list_data:
        if '*' in val:
            target = val.split('*(')
            data_map[f'({target[1]}'] = target[0]
        else:
            data_map['(x**0)'] = val

    return data_map

def add_data(data_first:dict, data_second:dict):
    list_keys =[]
    result_value = []
    for k, v in data_first.items():
        if not k in list_keys:
            list_keys.append(k)

    for k, v in data_second.items():
        if not k in list_keys:
            list_keys.append(k)

    list_keys.sort(reverse=True)

    for val in list_keys:
        result = int(data_first.get(val, 0)) + int(data_second.get(val, 0))

        if result:
            result_value.append(f'{result}*{val}' if not '0' in val else f'{result}')

    return ' + '.join(result_value) + ' = 0'


data_first = get_data_from_file('task1.txt')
data_second = get_data_from_file('task2.txt')

map_first = get_data_map(data_first)
map_second = get_data_map(data_second)

result_value = add_data(map_first, map_second)
write_data_to_file('result.txt', result_value)
