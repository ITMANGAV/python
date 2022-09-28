# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
str_num=input('Введите вещественное число: ')
bak_str_num=str_num.replace('.','')
bak_str_num=bak_str_num.replace(',','')
sum=0
for i in bak_str_num:
    sum+=int(i)
print(sum)
