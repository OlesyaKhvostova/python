import copy


def num_translate_adv(value):
    translate_map = {'zero':'ноль','one':'один','two':'два','three':'три','four':'четыре',
                    'five':'пять','six':'шесть','seven':'семь','eight':'восемь','nine':'девять','ten':'десять'}
    result = translate_map.get(value.lower())
    if (result != None) and (value == value.title()):
        result = result.title()
    
    return result



values = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven']
values_title = copy.copy(values)

print(values_title)
for index in range(0,len(values_title)):
    values_title[index] = values_title[index].title()

values_title.append('tVELVE')

print(values_title)

for data in values:
    print(num_translate_adv(data))

print('\n')

for data in values_title:
    print(num_translate_adv(data))
