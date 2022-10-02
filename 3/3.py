l=["qwe", "asd", "zxc", "qwe", "ertqwe", "asd"]
print(*l)
num=input('Введите искомую строку: ')
if l.count(num)<2:
    print('-1')
else:
    i=l.index(num)
    print('Позиция второго вхождения -> ', l.index(num, i+1))
