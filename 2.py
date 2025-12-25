import math

x1 = float(input('Введите 1 точку '))
y1 = float(input('Введите 2 точку '))
x2 = float(input('Введите 3 точку '))
y2 = float(input('Введите 4 точку '))

distance = math.sqrt(((x1-x2)**2) + ((y1-y2)**2))
print(f'Евклидово расстояние = {distance}')
