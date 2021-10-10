values = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
value_outputs_var1 = []
value_outputs_var2 = []
# Variant 1
for text_value in values:
    is_digit = True
    is_fvalue = False
    for char_elem in text_value:
        if not digits.count(char_elem) :
            if char_elem == '.':
                is_fvalue = True
            elif char_elem != '+' and char_elem  != '-':
                is_digit = False

        if not is_digit:
            break

    if not is_digit or (is_fvalue and is_digit):
        value_outputs_var1.append(text_value)
    else:
        value_outputs_var1.append('"')
        if text_value[0] == '+' or text_value[0] == '-':
            value_outputs_var1.append('{0}{1:02d}'.format(text_value[0],int(text_value[1:100])))
        else:
            value_outputs_var1.append('{0:02d}'.format(int(text_value)))
        value_outputs_var1.append('"')

output_value = ''
index = 0
list_len_var1 = len(value_outputs_var1)
while index < list_len_var1:
    output_value += value_outputs_var1[index]
    if (value_outputs_var1[index] == '"'):
        output_value += value_outputs_var1[index + 1] + value_outputs_var1[index + 2]
        index += 2

    output_value += ' '
    index += 1
print(output_value)
# Variant 2
for text_value in values:
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

    if not is_digit or (is_fvalue and is_digit):
        value_outputs_var2.append(text_value + ' ')
    else:
        value_outputs_var2.append('"')
        if text_value[0] == '+' or text_value[0] == '-':
            value_outputs_var2.append('{0}{1:02d}'.format(text_value[0], int(text_value[1:100])))
        else:
            value_outputs_var2.append('{0:02d}'.format(int(text_value)))
        value_outputs_var2.append('" ')

print(''.join(value_outputs_var2))
