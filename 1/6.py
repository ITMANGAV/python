number=int(input('Введите число недели: '))
days=['Понедельник', 'Вторник', 'Среда', ' Четверг', 'Пятница', 'Суббота', 'Воскресение']
if 1>number or number>7:
    print("Error")
elif number>5:
    print(f'{days[number-1]} - выходной')
else:
    print(f'{days[number-1]} - рабочий')

