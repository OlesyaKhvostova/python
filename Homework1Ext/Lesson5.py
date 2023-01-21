import math
coords_a = input('Ввести координаты точки А через запятую x,y')
coords_b = input('Ввести координаты точки B через запятую x,y')
coords_list_a = list(map(float,coords_a.split(',')))
coords_list_b = list(map(float,coords_b.split(',')))
print(coords_list_a,' ',coords_list_b,' ',coords_b," ")
dist = float(math.sqrt((coords_list_b[0]-coords_list_a[0])**2+(coords_list_b[1]-coords_list_a[1])**2))
print(f'{dist}')



