
dict_out={0: ['Билан', 'Дима', '02', 'Полиция']}
def ReadFileRow(name_file):
    with open(name_file, 'r', encoding='utf8') as file1:
        f1=file1.readlines()
    bak=[]
    for i in f1:
        bak.append(i.split())
    return bak


def ReadFileCol(name_file):
    with open(name_file, 'r',  encoding='utf8') as file:
        spamreader = file.readlines()
        bak=[]
        sub_bak=[]
        for row in spamreader:
            if row!='\n':
                sub_bak.append(row[:-1])
                if len(sub_bak)==4:
                    bak.append(sub_bak)
                    sub_bak=[]
    return bak

def UpdataDict(new):
    global dict_out
    dict_bak=dict(zip(range(len(dict_out), len(new)+len(dict_out)), new))
    dict_out=dict(list(dict_out.items()) + list(dict_bak.items()))
    # for k, i in dict_out.items():
    #         print (f'{k} {i}')
    return dict_out


def PrintDict():
    print('PrintDict')
    if dict_out=='':
        print ('Справочник пуст')
    else:
        for k, i in dict_out.items():
            print (f'{k} {i}')

def WriteCol(name_file):
    with open(name_file, 'w', encoding='utf8') as file:
        for key, value in dict_out.items():
            for i in value:
                file.write(f'{i}\n')
            file.write('\n')

def WriteRow(name_file):
    file=open(name_file, 'w', encoding='utf8')
    for i in dict_out:
        print (*dict_out[i], file=file)
    file.closed
