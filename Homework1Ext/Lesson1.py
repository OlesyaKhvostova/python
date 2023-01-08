value = int(input('Вввести день недели ')) 
if 1 <= value < 6:
    print(f'день недели = {value} - рабочий')
elif value == 7 or value == 6:
    print(f'день недели = {value} - выходной')
else:
    print('введен неверный день')
    
