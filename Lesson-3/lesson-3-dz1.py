def num_translate(value):
    translate_map = {'zero':'ноль','one':'один','two':'два','three':'три','four':'четыре',
                    'five':'пять','six':'шесть','seven':'семь','eight':'восемь','nine':'девять','ten':'десять'}
    return translate_map.get(value.lower())


values = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven']
for data in values:
    print(num_translate(data))