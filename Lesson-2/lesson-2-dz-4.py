workers = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

def get_worker_name(text_data):
    props = text_data.split(' ')
    worker_name = props[-1].capitalize()
    return worker_name

for worker in workers:
    name = get_worker_name(worker)
    print(f'Привет,{name}!')
