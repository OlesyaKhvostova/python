def odd_num(count):
    for value in range(1, count + 1, 2):
        yield value


odd_num_gen = odd_num(15)
result = str()
while result != 'StopIteration':
    result = next(odd_num_gen, 'StopIteration')
    print(result)
