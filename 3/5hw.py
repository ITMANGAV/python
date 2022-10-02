n=int(input('Введите число n: '))
# def fib(n):
#     print(n)
#     if n == 0:
#         return 0
#     if n in [1,2]:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)

# fib(6)

x2 = [1,-1]
for i in range(2, n):
    x2.append(x2[-2]-x2[-1])
print(', '.join(str(y) for y in reversed(x2)), end=' ')
print( '0', end=' ')
x = [1,1]
for i in range(2, n):
    x.append(x[-1] + x[-2])
print(', '.join(str(y) for y in x))