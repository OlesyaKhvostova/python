values = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def is_digit_func(text):
    is_digit = True
    is_fvalue = False
    for char_elem in text_value:
        if not digits.count(char_elem):
            if char_elem == '.':
                is_fvalue = True
            elif char_elem != '+' and char_elem != '-':
                is_digit = False

        if not is_digit:
            break

    return (is_digit, is_fvalue)

values_count = len(values)
index = 0
while index < values_count:
    text_value = values[index]
    is_digit = True
    is_fvalue = False

    is_digit, is_fvalue = is_digit_func(text_value)

    if is_digit and not is_fvalue:
        if text_value[0] == '+' or text_value[0] == '-':
            values[index] = '{0}{1:02d}'.format(text_value[0], int(text_value[1:100]))
        else:
            values[index] = '{0:02d}'.format(int(text_value))
        values.insert(index + 1, '"')
        values.insert(index, '"')
        values_count += 2
        index += 2
    else:
        index += 1

output_value = ''
index = 0
list_len_var1 = len(values)
while index < list_len_var1:
    output_value += values[index]
    if (values[index] == '"'):
        output_value += values[index + 1] + values[index + 2]
        index += 2

    output_value += ' '
    index += 1
print(output_value)
