num=int(input('Введите число N: '))
rez=[]
sum=0
for i in range(1,num+1):
    x=(1+1/i)**i
    rez.append(x)
    sum+=x
print(f'{rez} сумма= {sum}')