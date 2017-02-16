def fibb(x):
    fib0 = 0
    fib1 = 1
    fibval = []
    for i in range (x):

        if i >= x: break

        fib = fib0+fib1
        fib0 = fib1
        fib1 = fib
        fibval.append(fib)

    return fibval

def showfibb(x):
    print(fibb(x))

showfibb(7)
