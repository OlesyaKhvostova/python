class MyEx(Exception):
    def __init__(self, value):
        self.value = value


input_value = ''
while input_value != 'q':
    try:
        input_value = input('Введите число:')
        dig_value = 0
        if input_value != 'q':
            dig_value = int(input_value)
            input_div = int(input('Введите делитель:'))

        if input_div == 0:
            raise MyEx(input_div)
    except ValueError:
        print(f'Не числовые данные')
    except MyEx as err:
        print(f'Некорректный делитель {err.value}')
    else:
        print(f'Результат: {dig_value/input_div}')


