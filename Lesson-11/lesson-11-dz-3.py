class OnlyDigitEx(ValueError):
    def __init__(self, error_text):
        self.error_text = error_text

    def __str__(self):
        return self.error_text


def is_digit(value):
    if value.isdigit():
        return 1
    else:
        try:
            float(value)
        except ValueError:
            raise OnlyDigitEx(f'{value} не является числом')
        else:
            return 2;


def main():
    input_data = ''
    collect_data = []
    while input_data != 'stop':
        input_data = input('Введите число ')
        try:
            input_data.isalpha()
            type = is_digit(input_data)
            if type == 1:
                value = int(input_data)
            else:
                value = float(input_data)

        except OnlyDigitEx as my_err:
            print(my_err)
        else:
            collect_data.append(value)

    print(collect_data)

if __name__ == '__main__':
    main()