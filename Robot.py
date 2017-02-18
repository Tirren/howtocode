def Name(x):
    x = input('Enter the name ')
    return x

N = Name(1)

def Count(y):
    return len(str(N))

def OddEven(z):
    if Count(2) % 2 == 0:
        return 'It is an even number'
    else: return 'It is an odd number'

def PrintRes(i):
    print('Hello ' + N + '!', 'You have ' + str(Count(1)) + ' characters in your name.', OddEven(1), sep='\n')

PrintRes(1)