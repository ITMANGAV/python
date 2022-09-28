# Напишите программу, в которой пользователь будет задавать две строки, а программа -
# определять количество вхождений одной строки в другой.
import random
random_str=''
for i in range(30):
    random_str+=chr(random.randrange(1072,1103))
print(random_str)
str=input('Введите искомую строку: ')
count=random_str.count(str)
print(f'Количество вхождений - {count}')
