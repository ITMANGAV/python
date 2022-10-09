def Read_Mnogochlen(name_file):
    with open(name_file, 'r') as file1:
        f1=file1.readline()
    dict={'x^0':0, 'x^1':0}
    bak=f1.split('=')
    bak=bak[0].split('+')
    for i in reversed(bak):
        if '^' in i:
            tmp=i.split('x')
            dict['x'+tmp[1]]=tmp[0]
    def X0x1(b):
        if b[-1]=='x':
            t=b.split('x')
            dict['x^1']=t[0]
        if b[-1]!='x' and '^' not in b:
            dict['x^0']=b
        return dict
    dict=X0x1(bak[-1])
    dict=X0x1(bak[-2])
    return dict
dict1=Read_Mnogochlen('5hw-file-1.txt')
dict2=Read_Mnogochlen('5hw-file-2.txt')
z={}
for i in dict1:
    if i in dict2:
        z[i]=int(dict1[i])+int(dict2[i])
    else:
        z[i]=dict1[i]
for i in dict2:
    if i not in dict1:
        z[i]=dict2[i]
mnog_out=''
for i in reversed(z):
    if 'x^1' in i:
        mnog_out+='+'+str(z[i])+'x'
    elif 'x^0' in i:
        mnog_out+='+'+str(z[i])
    else:
        mnog_out+='+'+str(z[i])+i
mnog_out+='=0'
# print (dict1)
# print (dict2)
# print (z)
with open('5hw-file-1.txt', 'r') as file1:
        f1=file1.readline()
with open('5hw-file-2.txt', 'r') as file2:
        f2=file2.readline()
print(f'Фаил №1: {f1}') 
print(f'Фаил №2: {f2}')      
print (f'Сумма: {mnog_out}')

