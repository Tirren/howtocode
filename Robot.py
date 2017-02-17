def Name(x):
    return input('Enter the name ')

def Count(y):
    return len(str(Name(1)))

def OddEven(z):
    if Count(2) % 2 == 0:
        return 'Number is even'
    else: return 'Number is odd'

def PrintRes(i):
    print(OddEven(1))

PrintRes(1)