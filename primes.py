i = 2
n = 200

while True:
    f = True
    j = 2
    while j < i:
        if not i % j: f = False
        j += 1
    if f: print(i, end=' ')
    i += 1

    if i==n:
     break

primes = {j for i in range(2, 10) for j in range(2*i, 100, i)}
no_primes = [x for x in range(2, 100) if x not in primes]
