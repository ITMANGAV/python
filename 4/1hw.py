import math
d=input('Введите класс точности, например 0.001, D = ')
d=d.split('.')
print(round(math.pi,len(d[1])))