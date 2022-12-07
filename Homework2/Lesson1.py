from decimal import Decimal

def variant_one(value: str) -> int:
    data = value.split('.')
    total = 0
    temp = data[1]
    for i in range(len(temp)):
        total += int(temp[i])

    return total

def variant_second(value: str) -> int:
    number = Decimal(value)
    target_value = number - int(number)
    total = 0
    for i in range(0,10):
        temp = target_value * 10
        total += int(temp)
        target_value = temp - int(temp)

    return total


input_data = input('введите вещественное число\n')
#input_data_float = float(input_data)

print(f'Сумма {variant_one(input_data)} вариант 1\n')
print(f'Сумма {variant_second(input_data)} вариант 2\n')
