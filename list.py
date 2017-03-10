a = [int(s) for s in input().split()]
b = [int(s) for s in input().split()]
def nlist(x):
    y = []
    sum1, sum2 = 0, 0
    for i in x:
        sum1 += i
    for i in range(1, len(x) - 1):
        sum2 += x[i]
    y.append(sum1)
    y.append(max(x))
    y.append(sum2)
    return print(y)

def ddlist(x):
    return print(list(set(x)))

def mlist(x, y):
    return print(x+y)

