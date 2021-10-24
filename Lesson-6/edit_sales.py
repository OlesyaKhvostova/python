import os


def edit_data(edit_pos, data):
    r_file = open('bakery.csv', 'r', encoding='utf-8')
    w_file = open('temp_bakery.csv', 'w', encoding='utf-8')

    valid_index = False
    curr_index = 0
    while True:
        out_data = r_file.readline()
        write_data = f'{data}\n'
        if not out_data:
            break
        curr_index += 1

        if edit_pos == curr_index:
            w_file.write(write_data)
            valid_index = True
        else:
            w_file.write(out_data)

    r_file.close()
    w_file.close()

    if valid_index:
        os.remove('bakery.csv')
        os.rename('temp_bakery.csv', 'bakery.csv')
    else:
        os.remove('temp_bakery.csv')


def main(argv):
    program, *args = argv

    if len(args) == 2:
        return edit_data(int(args[0]), args[1])
    else:
        return 1


if __name__ == '__main__':
    import sys
    exit(main(sys.argv))
