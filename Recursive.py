def y(x):
    if x == 1:
        return print(1)
    else:
        y(x-1)
    return print(x)
y(20)