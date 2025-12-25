minutes = int(input('Введите количество минут '))

hours = minutes // 60
minutes_left = minutes % 60

print(f'{minutes} минут - это {hours} час и {minutes_left} минут')
