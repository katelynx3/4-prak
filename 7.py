import math

seat_num = int(input('Введите свое место (1-36) '))
if 1 <= seat_num <= 36:
    compartment_num = math.ceil(seat_num / 4)
    print(f'Ваше купе: {compartment_num}')
else:
    print('Такого места нет')
