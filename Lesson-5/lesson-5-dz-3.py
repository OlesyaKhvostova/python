def info_gen(tutors, klasses):
    for index in range(0,len(tutors)):
        klass = None
        if (index < len(klasses)):
            klass = klasses[index]

        yield (tutors[index],klass)


tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена', 'Станислав', 'Владислав'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]

info_class_gen = info_gen(tutors,klasses)
print(type(info_class_gen))
result = str()
while result != 'StopIteration':
    result = next(info_class_gen, 'StopIteration')
    print(result)
