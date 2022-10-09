import random
k=5
str_out=str(random.randrange(0,100))+'x^'+str(k)
for i in range(k-1,1,-1):
    num=random.randrange(0,100)
    str_out+=' + '+str(num)+'x^'+str(i)
str_out+=' + '+str(random.randrange(0,100))+'x'
str_out+=' + '+str(random.randrange(0,100))+' = 0'
with open('4hwfile.txt', 'w') as file:
    file.write(str_out)