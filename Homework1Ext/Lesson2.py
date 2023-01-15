def calc_left_part(x,y,z):
    return not(x or y or z)

def calc_right_part(x,y,z):
    return not x and not y and not z

print('x|y|z  not(x or y or z) = not x and not y and not z')
for x in range(2):
    for y in range(2):
        for z in range(2):
            left_part = calc_left_part(x,y,z)
            right_part = calc_right_part(x,y,z)
            print(f'{x}|{y}|{z}             {left_part} = {right_part}')
