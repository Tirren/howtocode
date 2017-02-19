Name = lambda: input('Enter the name ')

Count = lambda x: len(str(x))

def OddEven(y):
    if Count(y) % 2 == 0:
        return 'It is an even number'
    else:
        return 'It is an odd number'

def PrintNames():
    a = Name()
    b = Count(a)
    c = OddEven(b)
    return print('Hello ' + a + '!', 'You have ' + str(b) + ' characters in your name.', c, sep='\n')

PrintNames()