class Road:
    _length = 0
    _width = 0
    
    def __init__(self, length, width):
        self._length = length
        self._width = width
        
    def calculate(self, mass_by_sqr_metr, thickness):
        return self._length * self._width * mass_by_sqr_metr * thickness;
        

road_calc = Road(5000, 20)
massa_kg = road_calc.calculate(25, 5)
print(f'Масса = {massa_kg} кг')