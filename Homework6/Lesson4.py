def get_sign(curr_char, char_count):
    return f'{char_count}{curr_char}' if char_count > 1 else f'{curr_char}'

def compress(data:str):
    result = ''
    curr_char = data[0]
    char_count = 1
    for value in data[1:]:
        if value != curr_char:
            result += get_sign(curr_char,char_count)
            curr_char = value
            char_count = 1
        else:
            char_count += 1

    result += get_sign(curr_char,char_count)
    return result

def decompress(data:str):
    result = ''
    curr_char = ''
    for val in data:
        if val.isdigit():
            curr_char += val
        else:
            result += val * (int(curr_char) if len(curr_char) else 1)
            curr_char = ''

    return result

test_data = 'dddffffffffffffhjleeeirrrrtttt'
comress_data = compress(test_data)
decompress_data = decompress(test_data)

print(f'Original = {test_data}\n')
print(f'CompressData = {comress_data}\n')
print(f'DecompressData = {decompress_data}\n')
