d =int(input('Введите число недели: '))
if 1>d or d>7:
    print ('Введенно некоректное число')
else:
    if d>5:
        print ('Да')
    else:
        print ('Нет')
