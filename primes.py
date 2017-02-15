i = 2
while i < 200:
    f = True
    j = 2
    while j < i:
        if not i % j: f = False
        j += 1
    if f: print(i, end=' ')
    i += 1
