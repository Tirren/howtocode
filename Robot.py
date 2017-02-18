def Name(x):
    x = input('Enter the name ')
    return x

N = Name(True)

def Count(y):
    return len(str(N))

def OddEven(z):
    if Count(True) % 2 == 0:
        return 'It is an even number'
    else: return 'It is an odd number'

def PrintRes(i):
    print('Hello ' + N + '!', 'You have ' + str(Count(True)) + ' characters in your name.', OddEven(True), sep='\n')

PrintRes(True)