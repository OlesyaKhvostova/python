class Matrix:
    def __init__(self, data : list(list())):
        self.values = data

    def __str__(self):
        values_str = ''
        for list_val in self.values:
            for val in list_val:
                values_str += f'{val:5}'
            values_str += '\n'

        return values_str

    def __add__(self, other):
        if (type(other) == Matrix):
            for row_v in range(len(self.values)):
                if (len(other.values) != len(self.values)):
                    raise ValueError

                for col_v in range(len(self.values[row_v])):
                    if (len(other.values[row_v]) != len(self.values[row_v])):
                        raise ValueError

                    self.values[row_v][col_v] += other.values[row_v][col_v]

        return self



data = [[3,22,1],[16,5,24],[9,8,17]]
add_data = [[10,100,10],[100,10,100],[10,10,100]]

mtrx = Matrix(data)
add_mtrx = Matrix(add_data)

print(mtrx)
print(add_mtrx)

mtrx += add_mtrx
print(mtrx)