def Name(x):
    x = input('Enter the name ')
    return x

def Count(y):
    return len(str(Name(1)))

def OddEven(z):
    if Count(2) % 2 == 0:
        return 'It is an even number'
    else: return 'It is an odd number'

def PrintRes(i):
    print('Hello ' + Name(1) + '!', 'You have ' + str(Count(1)) + ' characters in your name.', OddEven(1), sep='\n')

PrintRes(1)