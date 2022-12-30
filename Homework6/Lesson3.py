#3.Создайте программу для игры в ""Крестики-нолики"".

import random
import time

current_player = 1
game_regime = 1

game_index_field = [['1','2','3'],['4','5','6'],['7','8','9']]

game_field = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
index_dict = {1:(0,0), 2:(0,1), 3:(0,2), 4:(1,0), 5:(1,1), 6:(1,2), 7:(2,0), 8:(2,1), 9:(2,2)}

win_dict = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]

def check_cell(index, sign = ' '):
    return game_field[index_dict[index][0]][index_dict[index][1]] == sign

def set_cell(index, player):
    game_field[index_dict[index][0]][index_dict[index][1]] = 'x' if player == 1 else 'o'

def print_field(game_index_field, game_field):
    print('---------', '    ', '---------')
    for i in range(0, 3):
        space_tab = '    ' if i != 1 else ' => '
        print(' | '.join(game_field[i]), space_tab, ' | '.join(game_index_field[i]))
        print('---------', '    ', '---------')

#print_field(game_index_field, game_field)

def reset_game():
    global game_field
    global current_player
    current_player = 1 if random.randint(0, 100) < 49 else 2

    for i in range(0,3):
        for j in range(0,3):
            game_field[i][j] = ' '

def check_win():
    global current_player
    global index_dict
    #win_dict = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
    check_sign = 'x' if current_player == 1 else 'o'
    for value in win_dict:
        list_data = list(filter(lambda cell:game_field[index_dict[cell][0]][index_dict[cell][1]] == check_sign, value))
        if len(list_data) == 3:
            return True

    return False

def enter_player():
    global current_player
    global game_index_field
    global game_field
    print_field(game_index_field, game_field)
    correct = False
    while not correct:
        cell_index = int(input(f'Игрок номер {current_player},\nВведите номер ячейки от 1 - 9\n'))
        if not check_cell(cell_index):
            print('Ячейка уже занята')
        else:
            correct = True

    return cell_index

def enter_ai():

    print('Выбирает Бот...\n')
    time.sleep(2)

    valid_cell = list(filter(check_cell, [i for i in range(1,10)]))
    cell_index = random.randint(0, len(valid_cell))

    print(f'Бот выбрал {cell_index} ячейку\n')
    return cell_index

def play():
    global current_player
    has_winner = False
    while not has_winner:
        cell_index = -1

        if game_regime == 1 or current_player == 2:
            cell_index = enter_player()
        elif current_player == 1:
            cell_index = enter_ai()

        set_cell(cell_index, current_player)

        has_winner = check_win()
        if has_winner:
            print(f'Игрок {current_player} выиграл, Поздравляем!!!\n')
        else:
            valid_cell = list(filter(check_cell, [i for i in range(1, 10)]))
            if len(valid_cell):
                current_player = 2 if current_player == 1 else 1
                print(f'Играем дальше\n')
            else:
                has_winner = True
                print(f'Ничья\n')


def select_state():
    state = input('Нажмите: p для начала следующей игра\nq - для выхода\n')
    return state

game_regime = int(input('Введите режим игры:\n1 - игрок vs игрок;\n2 - игрок vs AI\n'))
state = 'p' # play
while state == 'p':
    reset_game()
    print('Случайным образом выбирается кто ходит первый\n')
    print('Выбираем...\n')
    print(f'Первым будет ходить {current_player}\n')
    play()
    state = select_state()


