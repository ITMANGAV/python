# Задать список из N элементов, заполненных числами из [-N, N]. Найти произведение элементов
# на указанных позициях. Позиции хранятся в списке positions - создайте этот список (например:
# positions = [1, 3, 6]).
num=int(input('Введите положительное число N: '))
sec_num=num*-1
rez=[]
position=[1,3,6]
sum=0
for i in range(sec_num,num+1):
    rez.append(i)
for j in position:
    sum+=rez[j]
print(f'{rez} сумма= {sum}')