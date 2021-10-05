for i in range(1,101):
    text = ''
    if i >= 10 and i < 20:
        text = 'процентов'
    else:
        value = i % 10
        if value == 1:
            text = 'процент'
        elif value >= 2 and value <= 4:
            text = 'процента'
        else :
            text = 'процентов'

    print(f'{i} {text}')