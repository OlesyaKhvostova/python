import uuid
import random
import copy

class EquipWarehouse:
    eq_base = {'Printer': [], 'Scaner': [], 'Xerox': []}
    def __init__(self):
        self.warehouse = copy.deepcopy(EquipWarehouse.eq_base)
        self.subdivs_eq = dict()

    def __str__(self):
        return (f"На складе имеется:\nПринтеров = {len(self.warehouse[Printer.__name__])} шт\n \
Cканеров = {len(self.warehouse[Scaner.__name__])} шт\n \
Ксероксов = {len(self.warehouse[Xerox.__name__])} шт\n")

    def fill_warehouse(self):
        for _ in range(20):
            if _ < 6:
                self.add_equip_to_warhouse(f'{Printer.__name__}', Printer(uuid.uuid1(), f'{Printer.__name__}_{_}',\
                                                                              random.randrange(1, 10, 1) % 2,\
                                                                              random.randrange(1, 10, 1) % 2))
            elif _ < 14:
                self.add_equip_to_warhouse(f'{Scaner.__name__}',Scaner(uuid.uuid1(), f'{Scaner.__name__}_{_}', \
                                                                       random.randrange(1, 5, 1),\
                                                                        random.randrange(1, 10, 1) % 2))
            else:
                self.add_equip_to_warhouse(f'{Xerox.__name__}', Xerox(uuid.uuid1(), f'{Xerox.__name__}_{_}',\
                                                                          random.randrange(1, 10, 1) % 2,\
                                                                          random.randrange(1, 10, 1) % 2))


    @property
    def get_printer_info(self):
        return f'************\n'.join(map(str,[obj for obj in self.warehouse[Printer.__name__]]))


    @property
    def get_scaner_info(self):
        return f'************\n'.join(map(str, [obj for obj in self.warehouse[Scaner.__name__]]))


    @property
    def get_xerox_info(self):
        return f'************\n'.join(map(str,[obj for obj in self.warehouse[Xerox.__name__]]))

    def get_subdiv_info(self, subdiv_name):
        subdiv_use = self.subdivs_eq[subdiv_name]
        return f'{subdiv_name} использует:\n' + f'\n'.join([f'{key} = {len(subdiv_use[key])}' for key in subdiv_use.keys()]) + '\n'

    def add_equip_to_warhouse(self, obj_type, object):
        self.warehouse[obj_type].append(object)


    """Формат словаря {'Printer': count, 'Scaner': count, 'Xerox': count}"""
    def add_eqp_to_subdiv(self, sub_div_name, params: dict()):
        for key, val in params.items():
            if not (key == Printer.__name__ or key == Scaner.__name__ or key == Xerox.__name__):
                print('Неправильный тип устроства')
                continue

            for index in range(val):
                obj = self.warehouse[key].pop()
                if not sub_div_name in self.subdivs_eq:
                    self.subdivs_eq[sub_div_name] = copy.deepcopy(EquipWarehouse.eq_base)

                self.subdivs_eq[sub_div_name][key].append(obj)

class OfficeEquipment:
    def __init__(self, equip_id, name):
        self.equip_id = equip_id
        self.name = name


class Printer(OfficeEquipment):
    def __init__(self, equip_id, name, is_color, is_laser):
        self.equip_id = equip_id
        self.name = name
        self.is_color = is_color
        self.is_laser = is_laser


    def __str__(self):
        return f'Name = {self.name}\nId = {self.equip_id}\nColor = {self.is_color}\nLaser = {self.is_laser}\n'

class Scaner(OfficeEquipment):
    def __init__(self, equip_id, name, scan_format, scan_type):
        self.equip_id = equip_id
        self.name = name
        self.scan_format = scan_format
        self.scan_type = scan_type


    def __str__(self):
        return f'Name = {self.name}\nId = {self.equip_id}\nFormat = {self.scan_format}\nType = {self.scan_type}\n'


class Xerox(OfficeEquipment):
    def __init__(self, equip_id, name, xer_format, is_office):
        self.equip_id = equip_id
        self.name = name
        self.xer_format = xer_format
        self.is_office = is_office


    def __str__(self):
        return f'Name = {self.name}\nId = {self.equip_id}\nFromat = {self.xer_format}\nOffice = {self.is_office}\n'


warhouse = EquipWarehouse()
warhouse.fill_warehouse()

print(warhouse)
warhouse.add_eqp_to_subdiv('Приемная', {Printer.__name__:2,Xerox.__name__:1})
print(warhouse)
warhouse.add_eqp_to_subdiv('Кадры', {Printer.__name__:3,Scaner.__name__:2})
print(warhouse)
warhouse.add_eqp_to_subdiv('Пиар', {Xerox.__name__:3,Scaner.__name__:1})
print(warhouse)

print(warhouse.get_printer_info)
print(warhouse.get_scaner_info)
print(warhouse.get_xerox_info)

print(warhouse.get_subdiv_info('Приемная'))
print(warhouse.get_subdiv_info('Кадры'))
print(warhouse.get_subdiv_info('Пиар'))



