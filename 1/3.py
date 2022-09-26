number=int(input('Введите число N: '))
num=abs(number)
second_num=num*-1
while num>second_num:
    print (num,',', end=' ')
    num-=1
print(second_num)