
import Personal as per


def input_choice():
    while True:
        choice=input('1-Просмотреть базу 2-Добавить запись 3-Удалить запись 4-Найти запись 5-Изменить запись q-Выход: ')
        if choice=='1':
            per.preview_base()
        elif choice=='2':
            n=input('Введите имя сотрудника: ')
            ln=input('Введите фамилию сотрудника: ')
            p=input('Введите должность сотрудника: ')
            s=int(input('Введите размер зарплаты: '))
            b=int(input('Введите размер премии: '))
            per.add_record(n,ln,p,s,b)
        elif choice=='3':
            id=int(input('Введите id: '))
            per.delete_record(id)
        elif choice=='4':
            name=input('Введите имя сотрудника: ')
            per.find_record(name)
        elif choice=='5':
            id=int(input('Введите id сотрудника: '))
            sal=int(input('Введите размер новой зарплаты: '))
            per.update_record(sal, id)
        elif choice=='q':
            print('Выход')
            break
        else:
            print ('Ошибка ввода параметра')
