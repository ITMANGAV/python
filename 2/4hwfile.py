num=int(input('Введите положительное число N: '))
sec_num=num*-1
rez=[]
sum=0
for i in range(sec_num,num+1):
    rez.append(i)
position=open('4hwfile.txt', mode='r', encoding='utf-8')
for j in position:
    if int(j)>len(rez):
        print('Error')
    else:
        print(j.strip())
        sum+=rez[int(j)]
print(f'{rez} сумма= {sum}')