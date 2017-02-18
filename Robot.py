def Name():
    x = input('Enter the name ')
    y = str(x)
    def Count(y):
        return len(y)
    def OddEven():
            if Count(y) % 2 == 0:
                return 'It is an even number'
            else:
                return 'It is an odd number'
    return print('Hello ' + y + '!', 'You have ' + str(Count(y)) + ' characters in your name.', OddEven(), sep='\n')

Name()

