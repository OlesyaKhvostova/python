quater = int(input('Введите номер четверти\n'))

if quater >= 1 and quater <= 4:
    if quater == 1:
        print('Для 1 четверти диапазоны: X (0:INF) Y (0:INF)')
    elif quater == 2:
        print('Для 2 четверти диапазоны: X (-INF:0) Y (0:INF)')
    elif quater == 3:
        print('Для 3 четверти диапазоны: X (-INF:0) Y (-INF:0)')
    elif quater == 4:
        print('Для 4 четверти диапазоны: X (0:INF) Y (-INF:0)')
else:
    print('Значение не валидное')
