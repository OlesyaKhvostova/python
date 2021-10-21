src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]


def get_uniq(src):
    uniq_values = set()
    all_val = set()

    for val in src:
        if val not in all_val:
            uniq_values.add(val)
        else:
            uniq_values.discard(val)

        all_val.add(val)

    return uniq_values


def get_uniq_gn(src):
    uniq_values = get_uniq(src)
    for val in src:
        if (val in uniq_values):
            yield val


uniq_gen = get_uniq_gn(src)
uniq_elems = list(uniq_gen)
for val in uniq_elems:
    print(val)