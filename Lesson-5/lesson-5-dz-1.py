def odd_num(count):
    for value in range(1, count + 1, 2):
        yield value


odd_num_gen = odd_num(15)
print(next(odd_num_gen, 'StopIteration'))
print(next(odd_num_gen, 'StopIteration'))
print(next(odd_num_gen, 'StopIteration'))
print(next(odd_num_gen, 'StopIteration'))
print(next(odd_num_gen, 'StopIteration'))
print(next(odd_num_gen, 'StopIteration'))
print(next(odd_num_gen, 'StopIteration'))
print(next(odd_num_gen, 'StopIteration'))
print(next(odd_num_gen, 'StopIteration'))