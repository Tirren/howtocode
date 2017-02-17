Name = input('Enter the username ')
Count = len(str(Name))
if Count % 2 == 0:
    number = 'even'
    print('Hi ' + Name + '!', 'You have ' + str(Count) + ' characters in your name.', 'It is an ' + number + ' number.', sep='\n')
else:
    number = 'uneven'
    print('Hi ' + Name + '!', 'You have ' + str(Count) + ' characters in your name.', 'It is an ' + number + ' number.', sep='\n')

