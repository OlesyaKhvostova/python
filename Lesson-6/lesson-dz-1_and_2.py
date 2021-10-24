users_dict = dict()
req_params = list()


def append_user_id(users_dict, value):
    if value in users_dict:
        users_dict[value] += 1
    else:
        users_dict[value] = 1


def find_spamer(spamers_dict):
    values = list(spamers_dict.values())
    keys = list(spamers_dict.keys())
    index = values.index(max(values))
    return (keys[index], values[index])


def get_tuple_params(first_list, second_list):
    ip_param = first_list.split(' ')[0]
    _params = second_list.split(' ')
    return (ip_param, _params[0], _params[1])


def get_params_form_file(users_dict, req_params):
    file = open('nginx_logs.txt', 'r', encoding='utf-8')
    while True:
        text_line = file.readline()
        if not text_line:
            break

        params = text_line.split('"')
        if len(params) > 2:
            value = get_tuple_params(params[0],params[1])
            req_params.append(value)
            append_user_id(users_dict, params[0].split(' ')[0])


get_params_form_file(users_dict, req_params)
print(find_spamer(users_dict))
print(users_dict)
