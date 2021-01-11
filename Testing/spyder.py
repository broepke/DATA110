def fib(n):
    '''
    Generates a Fib Sequence

    Parameters
    ----------
    n : TYPE
        DESCRIPTION.

    Returns
    -------
    fibs : TYPE
        DESCRIPTION.

    '''
    fibs = []
    a, b = 0, 1
    while a < n:
        fibs.append(a)
        a, b = b, a+b
    return fibs


q = fib(1000)

print(q)
