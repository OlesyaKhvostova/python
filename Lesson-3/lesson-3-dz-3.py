def thesaurus(*args):
    names_dict = dict()

    for name in args:
        if not name[0] in names_dict:
            names_dict[name[0]] = list({name})
        else:
            names_dict[name[0]].append(name)

    return names_dict



names_dict = thesaurus("Иван", "Мария", "Петр", "Илья", "Влад", "Алексей", "Сергей", "Сава","Саня","Андрей")

print(names_dict)
