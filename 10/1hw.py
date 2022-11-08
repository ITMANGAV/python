from functools import reduce


def decorator(func):
    cach={}
    def wrapper(*args):
        key=args
        if key not in cach:
            cach[key]=func(*args)
        print (cach)
        return cach[key]
    return wrapper



@decorator
def seq(n):
    rez=list(map(lambda i: (i+1)**i, range(0,n+1)))
    return rez


print (seq(5))
