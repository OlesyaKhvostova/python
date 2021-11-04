class Car:
    def __init__(self):
        self.speed = 0
        self.color = ''
        self.name = ''
        self.is_police = False

    def go(self):
        print('Поехала')

    def stop(self):
        print('Остановилась')

    def turn(self, direction):
        print(f'повернула {direction}')

    def show_speed(self):
        print(self.speed)

class TownCar(Car):
    def __init__(self, speed, color):
        self.speed = speed
        self.color = color
        self.name = 'TownCar'


    def show_speed(self):
        if self.speed > 60:
            print('Превышение скорости')
        else:
            Car.show_speed(self)

class WorkCar(Car):
    def __init__(self, speed, color):
        self.speed = speed
        self.color = color
        self.name = 'WorkCar'


    def show_speed(self):
        if self.speed > 40:
            print('Превышение скорости')
        else:
            Car.show_speed(self)


class SportCar(Car):
    def __init__(self, speed, color):
        self.speed = speed
        self.color = color
        self.name = 'SportCar'


class PoliceCar(Car):
    def __init__(self, speed, color):
        self.speed = speed
        self.color = color
        self.name = 'PoliceCar'
        self.is_police = True


town_car = TownCar(30,'синий')
town_car_fast = TownCar(70,'красный')
sport_car = SportCar(100,'желтый')
work_car = WorkCar(30,'синий')
police_car = PoliceCar(70,',белосиний')

town_car_fast.show_speed()
print(f'{town_car_fast.name} {town_car_fast.color}')
town_car.show_speed()
print(f'{town_car.name} {town_car.color}')
sport_car.show_speed()
print(f'{sport_car.name} {sport_car.color}')
work_car.show_speed()
print(f'{work_car.name} {work_car.color}')
police_car.show_speed()
print(f'{police_car.name} {police_car.color}')





