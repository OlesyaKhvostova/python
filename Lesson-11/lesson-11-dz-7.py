class ComplexNumber:
    def __init__(self, real_part, mnim_part):
        self.real_part = real_part
        self.mnim_part = mnim_part

    def __add__(self, other):
        self.real_part += other.real_part
        self.mnim_part += other.mnim_part
        return self

    def __mul__(self, other):
        real_part = self.real_part * other.real_part - self.mnim_part * other.mnim_part
        mnim_part = self.real_part * other.mnim_part + other.real_part * self.mnim_part
        self.real_part = real_part
        self.mnim_part = mnim_part
        return self

    def __str__(self):
        return f'{self.real_part}{self.mnim_part:+}i'


complex_1 = ComplexNumber(10, 20)
complex_2 = ComplexNumber(5, 10)
complex_3 = ComplexNumber(2, 4)

complex_1 += complex_2
print(complex_1)

complex_2 *= complex_3  # (2*5 - 4*10) + (5*4 + 2*10)i
print(complex_2)
print('Правльный результат: -30 + 40i')