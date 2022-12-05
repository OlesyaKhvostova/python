print(f'X Y Z |  ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z | Result')
for x in range(0,2):
    for y in range(0,2):
        for z in range(0,2):
            left_value = not(x or y or z)
            right_value = (not x) and (not y) and (not z)
            result = left_value == right_value
            print(f'{x} {y} {z} |         {left_value} = {right_value}         | {result}')