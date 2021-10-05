list_data = []
for i in range(1,1001, 2):
    list_data.append(i**3)

final_summ = 0
for index in range(0,2):
    for value in list_data:
        value += index * 17
        curr_value = value
        summ_value = 0
        for i in range(9,0, -1):
            divider = (10 ** i)
            if (value >= divider):
                data = value // divider
                summ_value += data
                value -= data * divider
        summ_value += value

        if not summ_value % 7:
            final_summ += curr_value
        value = curr_value + 17

    print(final_summ)