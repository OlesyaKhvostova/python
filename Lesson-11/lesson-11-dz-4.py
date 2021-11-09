class EquipWarhouse:
    def __init__(self):
        self.Warhouse = {'Printer': {}, 'Scaner': {}, 'Xerox': {}}


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