from utils import currency_rates,convert_value

def main(argv):
    program, *argv = argv
    params = list(map(str,argv))
    
    for value in params:
        print(f"{value} = {convert_value(currency_rates(value))}")


if __name__=='__main__':
    import sys
    
    exit(main(sys.argv))