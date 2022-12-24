#2.Создайте программу для игры с конфетами человек против человека.
#
#Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется
# жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
#
#a) Добавьте игру против бота
#
#b) Подумайте как наделить бота ""интеллектом""

import random
import time
current_candies = 2021
current_player = 1
game_regime = 1

def restart():
    global current_candies
    global current_player
    current_candies = 2021
    current_player = 1 if random.randint(0, 100) < 49 else 2

def enter_candies():
    global current_player
    global current_candies
    cur_value = min(28, current_candies)
    candies = int(input(f'Игрок номер {current_player},\nсколько конфет вы заберете от 1 до {cur_value}:\n'))

    if candies < 1 or candies > cur_value:
        print('Ошибка:Неверное число конфет, выставим 1\n')
        candies = 1

    return candies

def enter_ai():
    global current_candies
    print('Выбирает Бот...\n')
    time.sleep(2)
    candies = random.randint(1, min(current_candies, 28))
    print(f'Бот забирает {candies} конфет\n')
    return candies

def play():
    global current_candies
    global current_player
    print(f'На столе {current_candies} конфет\n')
    while current_candies > 0:
        if game_regime == 1:
            candies = enter_candies()
        elif current_player == 1:
            candies = enter_ai()
        elif current_player == 2:
            candies = enter_candies()

        current_candies -= candies
        if current_candies == 0:
            print(f'Игрок {current_player} выиграл, Поздравляем!!!\n')
        else:
            current_player = 2 if current_player == 1 else 1
            print(f'На столе осталось {current_candies} конфет\n')

def select_state():
    state = input('Нажмите: p для начала следующей игра\nq - для выхода\n')
    return state

game_regime = int(input('Введите режим игры:\n1 - игрок vs игрок;\n2 - игрок vs AI\n'))

state = 'p' # play
while state == 'p':
    restart()
    print('Случайным образом выбирается кто ходит первый\n')
    print('Выбираем...\n')
    print(f'Первым будет ходить {current_player}\n')
    play()
    state = select_state()


