def val_checker(check_expr):
    def wraper(func):
        def _wrap(value):
            if (check_expr(value)):
                return func(value)
            else:
                raise ValueError(f'wrong val {value}')
        return _wrap
    return wraper


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x**3


print(calc_cube(5))
print(calc_cube(-5))
