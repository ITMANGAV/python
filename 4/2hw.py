num=int(input('Введите натуральное число N: '))
def Allmnog(n):
    all_pm=[]
    for i in range(2,n+1):
        m=0
        for j in range(2,i):
            if i%j==0:
                m=1
        if m==0:
            all_pm.append(i)
    return all_pm
allm=Allmnog(num)
def Mnog(n):
    mnogitile=[]
    k=0
    x=0
    while x<len(Allmnog(n)):
        if n%allm[x]==0:
            mnogitile.append(allm[x])     
            n//=allm[x]
            k=k+1
            x=0
        else:
            x+=1
    return mnogitile
print (f'Простые множители:  {Mnog(num)}')        
