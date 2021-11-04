class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self._income = {'wage':wage,'bonus':bonus}
        self.name = name
        self.surname = surname
        self.position = position


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']


worker_pos = Position('Иван', 'Петров', 'рабочий', 100, 50)
main_worker_pos = Position('Алексей', 'Федюк', 'рабочий', 200, 50)

print(f'Имя: {worker_pos.get_full_name()},Зарплата: {worker_pos.get_total_income()}')
print(f'Имя: {main_worker_pos.get_full_name()},Зарплата: {main_worker_pos.get_total_income()}')
