def main(argv):
    program, *args = argv

    value = args[0]
    with open('bakery.csv', 'a', encoding='utf-8') as out_file:
        out_file.write(f'{value}\n')

    return 0

if __name__ == '__main__':
    import sys
    exit(main(sys.argv))