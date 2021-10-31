def log_type_param(func):
    def wraper(*args):
        for value in args:
            print(type(value))
        func(*args)
    return wraper

@log_type_param
def func_print_value(*args):
    print(*args)

func_print_value(10)
func_print_value(100.23)
func_print_value(10, '123', 'temp')

