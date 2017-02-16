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

