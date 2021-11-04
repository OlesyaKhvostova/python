class Stationery:
    def __init__(self):
        self.title = ''

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def __init__(self):
        self.title = 'Pen'

    def draw(self):
        print(f'Рисует {self.title}')

class Pencil(Stationery):
    def __init__(self):
        self.title = 'Pencil'

    def draw(self):
        print(f'А теперь рисует {self.title}')

class Handle(Stationery):
    def __init__(self):
        self.title = 'Handle'

    def draw(self):
        print(f'А сейчас рисует {self.title}')



pen_obj = Pen()
pencil_obj = Pencil()
handle_obj = Handle()

pen_obj.draw()
pencil_obj.draw()
handle_obj.draw()

