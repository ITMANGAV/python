import dictionary as d
def menu():
    while True:   
        print( "\nГЛАВНОЕ МЕНЮ\n") 
        print( "1. Просмотреть все существующие контакты") 
        print( "2. Импортировать новые контакты из файла-строк (file-row.txt)") 
        print( "3. Импортировать новые контакты из файла-колонки (file-col.txt)") 
        print( "4. Экспортировать контакты строками")
        print( "5. Экспортировать контакты столбцами") 
        print( "6. Выход") 
        choice = input("Выберите пункт меню: ")
        if choice=='1':
            d.PrintDict()
        elif  choice=='2':
            l=d.ReadFileRow('file-row.txt')
            d.UpdataDict(l)
            print ('Успешно импортированно')
        elif  choice=='3':
            l=d.ReadFileCol('file-col.txt')
            d.UpdataDict(l)
            print ('Успешно импортированно')
        elif  choice=='4':
            d.WriteRow('out-row.txt')
            print ('Успешно экспортированно в out-row.txt')
        elif  choice=='5':
            d.WriteCol('out-col.txt')
            print ('Успешно экспортированно в out-col.txt')
        elif  choice=='6':
            break
        else:
            print('Ошибка в меню!')
            