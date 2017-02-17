Name = input('Enter the username ')
Count = len(str(Name))
if Count % 2 == 0:
    print('Hi ' + Name + '!', 'You have ' + str(Count) + ' characters in your name.', 'It is an even number.', sep='\n')
else:
    print('Hi ' + Name + '!', 'You have ' + str(Count) + ' characters in your name.', 'It is an uneven number.', sep='\n')

