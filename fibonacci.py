def fibb(x):
    fib0 = 0
    fib1 = 1
    fibval = []
    while True:

        fib = fib0 + fib1
        fib0 = fib1
        fib1 = fib
        if fib > x: break
        fibval.append(fib)

    return tuple(fibval)

def showfibb(x, y):
    print(y.join(str(x) for x in fibb(x)))
showfibb(50, ' | ')
