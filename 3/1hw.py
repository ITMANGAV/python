l=[1,3,5,7,9,10]
summa=0
for i in range(0, len(l)):
    if i%2==1:
        summa+=l[i]
print(summa)