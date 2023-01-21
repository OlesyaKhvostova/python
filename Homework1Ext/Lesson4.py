quarter_index = int(input('Ввести номер четверти'))
if quarter_index == 1:
    print('x=(0,+inf)')
    print('y=(0,+inf)')
elif quarter_index == 2:
    print('x=(-inf,0)')
    print('y=(0,+inf)')
elif quarter_index == 3:
    print('x=(-inf,0)')
    print('y=(-inf,0)')
elif quarter_index == 4:
    print('x=(0,inf)')
    print('y=(-inf,0)')
else:
    print('четверть определить невозможно')