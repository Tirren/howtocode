import numc

def Name():
    return input('Enter the name ')

def OddEven(y):
    if numc.Count(y) % 2 == 0:
        return 'It is an even number'
    else:
        return 'It is an odd number'

def PrintNames():
    a = Name()
    b = numc.Count(a)
    c = OddEven(b)
    return print('Hello ' + a + '!', 'You have ' + str(b) + ' characters in your name.', c, sep='\n')

PrintNames()