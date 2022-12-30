import os
last_id = 0
main_dict = {}

def menu():
    state = 1
    while state:
        print('1 - добавить пользователя\n\
        2 - показать словарь\n3 - сохранить словарь\n4 - загрузить словарь\n0 - Выход')
        state = int(input('Введите пункт:\n'))
        if state == 1:
            request_user_data()
        elif state == 2:
            show_dict()
        elif state == 3:
            file_name = input('Введите имя файла:\n')
            export_dict(file_name)
        elif state == 4:
            file_name = input('Введите имя файла:\n')
            import_dict(file_name)

def show_dict():
    print("")

def request_user_data():
    name = input('Введите имя:\n')
    sername = input('Введите фамилию:\n')\
    phone_number = input('Введите номер:\n')\
    description = input('Введите комментарий:\n')
    add_user(name, sername, phone_number, description)

def add_user(name, sername, phone_number, description):
    global last_id
    main_dict[last_id] = (name, sername, phone_number, description)
    last_id += 1

def get_user_id(name, sername):
    global main_dict
    for key,value in main_dict.items():
        if (value[0] == name and value[1] == sername)
            return key

    return -1

def remove_user(name, sername):
    id = get_user_id(name, sername)
    if id != -1:
        main_dict.pop(id)

def read_txt_format(main_dict, dict_file):
    global last_id
    user_data = []
    for line in dict_file:
        user_data.append(line)
        if len(user_data) == 5:
            main_dict[int(user_data[0])] = tuple(user_data[1:])
            last_id = int(user_data[0])
            user_data.clear()

def read_csv_format(main_dict, dict_file):
    global last_id
    for line in dict_file:
        user_data = line.split(';')
        main_dict[int(user_data[0])] = tuple(user_data[1:])
        last_id = int(user_data[0])

def write_txt_format(main_dict, dict_file):
    for key,value in main_dict.items:
        text = '\n'.join(value)
        dict_file.write(f'{key}\n{text}\n')

def write_csv_format(main_dict, dict_file):
    for key,value in main_dict.items:
        text = ';'.join(value)
        dict_file.write(f'{key};{text}\n')
def is_ext(file_name, ext):
    file_data = os.path.split(file_name)
    return file_data[1] == ext

def import_dict(file_name):
    global main_dict
    if len(main_dict):
        print('Ваши данные будут уничтожены')

    dict_file = open(file_name, 'r+')
    if is_ext(file_name,'txt'):
        read_txt_format(main_dict, dict_file)
    elif is_ext(file_name,'csv'):
        read_csv_format(main_dict, dict_file)
    else:
        print('Неизвестный формат файла')

    dict_file.close()

def export_dict(file_name):
    dict_file = open(file_name, 'w+')
    if is_ext(file_name,'txt'):
        write_txt_format(main_dict, dict_file)
    elif is_ext(file_name,'csv'):
        write_csv_format(main_dict, dict_file)
    else:
        print('Неизвестный формат файла')
    dict_file.close()