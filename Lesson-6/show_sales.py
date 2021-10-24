def show_data(begin_pos, end_pos):
    with open('bakery.csv', 'r', encoding='utf-8') as read_file:
        curr_index = 0
        while True:
            out_data = read_file.readline()
            if not out_data:
                break
            curr_index += 1

            if not begin_pos and not end_pos:
                print(out_data, end='')
            elif curr_index >= begin_pos and ( (end_pos and curr_index <= end_pos) or not end_pos):
                print(out_data,end='')



def main(argv):
    program, *args = argv

    if not len(args):
        show_data(0,0)
    elif len(args) == 1:
        show_data(int(args[0]),0)
    elif len(args) == 2:
        show_data(int(args[0]), int(args[1]))


if __name__ == '__main__':
    import sys
    exit(main(sys.argv))