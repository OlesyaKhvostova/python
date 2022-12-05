input_data = input('Введите день недели\n')
day_of_week = int(input_data)
if day_of_week >= 1 and day_of_week <= 7:
    if day_of_week == 6 or day_of_week == 7:
        print('Это выходной день')
    else:
        print('Это рабочий день')
else:
    print('Ошибка: такого дня нет')