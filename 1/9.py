n =int(input('Введите номер четверти: '))
if 1>n or n>4:
    print ('Введен некоректный номер четверти')
elif n==1:
    print ('x>0; y>0')
elif n==2:
    print ('x>0; y<0')
elif n==3:
    print ('x<0; y<0')
elif n==4:
    print ('x<0; y>0') 