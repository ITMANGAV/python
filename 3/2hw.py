l=[2, 3, 4, 5, 6, 1, 0]
rez=[]
for i in range(0,len(l)//2):
    rez.append(l[i]+l[-i-1])
print(rez)