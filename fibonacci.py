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

    return fibval

def showfibb(x):
    print(fibb(x))

showfibb(50)
