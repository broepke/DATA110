import numpy as np

def fib(n):
    fibs = []
    a, b = 0, 1
    while a < n:
        fibs.append(a)
        a, b = b, a+b
    return fibs


q = fib(10000)

print(q)

def foo(x,b):
    if x > b:
        print(x)
    else:
        print(b)
        
x = 1
b = 2

foo(x,b)

q = np.array(q)

print(type(q))

print(q)

my_dict = {"a": "foo",
           "b": "bar",
           "c": [[1,2],
               [3,4]]}

print(my_dict)