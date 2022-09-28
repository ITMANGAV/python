# Реализовать алгоритм перемешивания списка.
#num=input('Введите через запятую значения списка: ')
num='0, 1, 2, 3, 4, 5'
list=num.split(',')
for i in range(0,len(list)-1,2):
    bak=list[i]
    list[i]=list[i+1]
    list[i+1]=bak
print(list)