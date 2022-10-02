import time
t=time.time_ns()
k1=t%10000//1000
k2=t%1000//100
for i in [1,2]:
    n1=abs(k2-k1+i)
    n2=abs((k2+k1-i)%10)
    n3=(n2+n1+i)%10
print (n1)
print (n2)
print (n3)