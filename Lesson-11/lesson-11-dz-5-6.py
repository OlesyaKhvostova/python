import uuid
import random

class EquipWarhouse:
    def __init__(self):
        self.Warhouse = {'Printer': {}, 'Scaner': {}, 'Xerox': {}}


    def __str__(self):
        return (f"На складе имеется:\nПринтеров = {len(self.Warhouse['Printer'])} шт\n \
Cканеров = {len(self.Warhouse['Scaner'])} шт\n \
Ксероксов = {len(self.Warhouse['Xerox'])} шт\n")


    def add_equip_to_warhouse(self, obj_type, object):
        self.Warhouse[obj_type][object.equip_id] = object


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


class Scaner(OfficeEquipment):
    def __init__(self, equip_id, name, scan_format, scan_type):
        self.equip_id = equip_id
        self.name = name
        self.scan_format = scan_format
        self.scan_type = scan_type


class Xerox(OfficeEquipment):
    def __init__(self, equip_id, name, xer_format, is_office):
        self.equip_id = equip_id
        self.name = name
        self.xer_format = xer_format
        self.is_office = is_office


warhouse = EquipWarhouse()

for _ in range(20):
    if _ < 6:
        warhouse.add_equip_to_warhouse('Printer',Printer(uuid.uuid1(), f'Printer_{_}', random.randrange(1,10,1)%2, random.randrange(1,10,1)%2))
    elif _ < 14:
        warhouse.add_equip_to_warhouse('Scaner',Scaner(uuid.uuid1(), f'Scaner_{_}', random.randrange(1,5,1), random.randrange(1,10,1)%2))
    else:
        warhouse.add_equip_to_warhouse('Xerox',Xerox(uuid.uuid1(), f'Xerox{_}', random.randrange(1,10,1)%2, random.randrange(1,10,1)%2))

print(warhouse)



