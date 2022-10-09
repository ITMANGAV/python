l=[2,2,3,4,5,4]
m=set(l) # {2,3,4,5}
for i in m:
    k=0
    for j in l:
        if j==i:
            k+=1
    if k<2:
        print(i)