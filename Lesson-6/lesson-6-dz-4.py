user_file_name = 'users.csv'
hobby_file_name = 'hobby.csv'

def init_files(user_file_name, hobby_file_name):
    user_file = open(user_file_name, 'w', encoding='utf-8')
    user_file.write('Иванов,Иван,Иванович\n')
    user_file.write('Петров,Петр,Петрович\n')
    user_file.write('Серегин,Сергей,Иванович\n')
    user_file.write('Александров,Саня,Петрович\n')
    user_file.write('Атласов,Эдурад,Антонович\n')
    user_file.write('Антон,Алексей,Сергеич\n')
    user_file.close()

    hobby_file = open(hobby_file_name, 'w', encoding='utf-8')
    hobby_file.write('скалолазанье,охота\n')
    hobby_file.write('рыбалка,охота\n')
    hobby_file.write('прогулки\n')
    hobby_file.write('путешествие\n')
    hobby_file.write('компьютеры\n')
    hobby_file.write('игры\n')
    hobby_file.close()


def create_save_dict(user_file_name, hobby_file_name):
    result = 0
    user_file = open(user_file_name, 'r', encoding='utf-8')
    hobby_file = open(hobby_file_name, 'r', encoding='utf-8')
    user_hobby_file = open('user_hobby.csv', 'w', encoding='utf-8')

    while True:
        user = user_file.readline().strip('\n');
        hobby = hobby_file.readline().strip('\n');

        if not user and hobby:
            result = 1
            break
        elif user and not hobby:
            hobby = None
        elif not user:
            break

        user_hobby_file.write(f'{user}: {hobby}\n')

    user_file.close()
    hobby_file.close()
    user_hobby_file.close()

    return result


def main():
    init_files(user_file_name, hobby_file_name)
    return create_save_dict(user_file_name, hobby_file_name)


if __name__ == '__main__':
    exit(main())
else:
    main()
