#Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
num=int(input('Введите число N: '))
rez=[1]
x=1
for i in range(1,num):
    x+=x*i
    rez.append(x)
print(rez)