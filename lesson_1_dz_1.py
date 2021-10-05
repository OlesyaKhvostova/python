input_data = '-10'
minute_sec = 60
hour_sec = 60 * minute_sec
day_sec = 24 * hour_sec

while input_data != '0':
    input_data = input('Введите период ')
    period = int(input_data)

    text = ''
    if period >= day_sec:
        days = period // day_sec
        period -= days * day_sec
        text = f'{days} дн '

    if period >= hour_sec:
        hours = period // hour_sec
        period -= hours * hour_sec
        text += f'{hours} час '

    if period >= minute_sec:
        minutes = period // minute_sec
        period -= minutes * minute_sec
        text += f'{minutes} мин '

    seconds = period
    text += f'{seconds} сек\n'
    print(text)


