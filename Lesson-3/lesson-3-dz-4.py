def thesaurus_adv(*args):
    names_dict = dict()

    for name in args:
        name_pair = name.split(' ')
        name_ch = name_pair[0][0]
        surname_ch = name_pair[1][0]

        if not surname_ch in names_dict:
            temp = dict({name_ch:list({name})})
            names_dict[surname_ch] = temp
        elif not name_pair[0][0] in names_dict[surname_ch]:
            names_dict[surname_ch].setdefault(name_ch,list({name}))
        else:
            names_dict[surname_ch][name_pair[0][0]].append(name)

    return names_dict



names_dict = thesaurus_adv("Иван Иванов", "Мария Страж","Маша Стол", "Петр Сидоров", "Илья Обухов", "Влад Сташев", "Алексей Оркский",
                       "Сергей Новый", "Сава Временный","Саня Подгорный","Андрей Летучий")

print(names_dict)
