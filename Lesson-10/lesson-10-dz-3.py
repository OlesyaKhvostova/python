from __future__ import division

class Cell:
    def __init__(self, count : int):
        self.count = count


    def __add__(self, other):
        self.count += other.count
        return self


    def __sub__(self, other):
        if (self.count - other.count < 0):
            print('Вычисление невозможно, разница отрицательная')
        else:
            self.count -= other.count

        return self


    def __mul__(self, other):
        self.count *= other.count
        return self


    def __floordiv__(self, other):
        self.count = int(self.count / other.count)
        return self


    def __truediv__(self, other):
        self.count = int(self.count / other.count)
        return self


    def make_order(self, order):
        out_data = ''
        last_cell = self.count
        while(last_cell > 0):
            if (last_cell - order < 0 ):
                out_data += str().rjust(last_cell, '*')
            else:
                out_data += str().rjust(order, '*')
                out_data += '\n'

            last_cell -= order
        return out_data


cell_10 = Cell(10)
cell_4 = Cell(4)
print(Cell.make_order(cell_10, 4))
cell_10 /= cell_4
print(Cell.make_order(cell_10, 4))
cell_10 *= cell_4
print(Cell.make_order(cell_10, 4))
cell_10 += cell_4
print(Cell.make_order(cell_10, 5))
cell_10 -= cell_4
print(Cell.make_order(cell_10, 7))