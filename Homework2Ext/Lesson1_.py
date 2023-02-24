from decimal import Decimal

def calculate(value : str) -> int:
    start_value = Decimal(value)
    result = 0

    for i in range(0,10):
        temp_value = Decimal(start_value * 10)
        temp_result = int(temp_value)
        result += temp_result
        start_value = temp_value - temp_result

    return result

number = input("Введите вещественное число")
result = calculate(number)
print(f'{number} -> {result} ')
