x =int(input('Введите x = '))
y = int (input('Введите y = '))
if x==0:
    print ('Точка лежит на оси Х')
    exit()
if y==0:
    print ('Точка лежит на оси Y')
    exit()
if x>0:
    if y>0:
        print ('Zona 1')
    else:
        print ('Zona 2')
else:
    if y>0:
        print ('Zona 4')
    else:
        print ('Zona 3')