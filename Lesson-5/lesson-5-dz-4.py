src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]


def get_greater_gn(src):
    last_value = src[0]
    for value in src:
        if (last_value < value):
           yield value

        last_value = value


greater_gn = get_greater_gn(src)

print(type(greater_gn))

greater_gn = get_greater_gn(src)
for val in greater_gn:
    print(val)