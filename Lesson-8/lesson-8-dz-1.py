import re

email_re = re.compile(r'(\w+)@(\w+.\w{2,6})')

def get_email_data(email_val):

    temp = email_re.findall(email_val)
    if (len(temp) == 1 and len(temp[0]) > 1):
        temp_data = {'username':temp[0][0], 'domain':temp[0][1]}
        return temp_data
    else:
        raise ValueError(f'wrong email: {email_val}')

input_data = ''
while input_data != 'q':
    in_data = input("Введите емейл: ")
    value = get_email_data(in_data)
    print(value)
