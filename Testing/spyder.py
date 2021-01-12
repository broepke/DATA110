def fib(n):
    fibs = []
    a, b = 0, 1
    while a < n:
        fibs.append(a)
        a, b = b, a+b
    return fibs


q = fib(10000)

vingprint(q)

# Thanks to some kids in Singapore
