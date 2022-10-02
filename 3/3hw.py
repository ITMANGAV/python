l=[1.1, 1.2, 3.71, 5.05, 10.01]
min=round(l[0]-l[0]//1,2)
max=min
for i in l:
    d=round(i-i//1,2)
    if d>max:
        max=d
    if d<min:
        min=d
print (l, max-min)