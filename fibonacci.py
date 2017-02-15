fib0 = 0
fib1 = 1

print(fib1, end=' ')
for i in range (200):
    fib = fib0 + fib1
    fib0 = fib1
    fib1 = fib
    print(fib, end=' ')
