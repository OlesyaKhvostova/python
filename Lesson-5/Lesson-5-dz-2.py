odd_num_gen = (value for value in range(1,15+1, 2))
result = str()
while result != 'StopIteration':
    result = next(odd_num_gen, 'StopIteration')
    print(result)
