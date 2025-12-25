stud = int(input('Введите количество школьников '))
orange = int(input('Введите количество мандаринов '))

orange_for_stud = orange // stud
ostatok = orange % stud
print(f'''Каждому школьнику достанется по {orange_for_stud} 
{ostatok} мандаринов останется''')
