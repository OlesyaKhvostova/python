cord_x = int(input('Ввести значение x\n'))
cord_y = int(input('Ввести значение y\n'))
if cord_x > 0 and cord_y > 0:
    print('точка координаты в 1 четверти')
elif cord_x < 0 and cord_y > 0:
    print('точка координаты во 2 четверти')
elif cord_x < 0 and cord_y < 0:
    print('точка координаты в 3 четверти')
elif cord_x > 0 and cord_y < 0:
    print('точка координаты в 4 четверти')
else:
    print('четверть определить невозможно')