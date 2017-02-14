from math import pi

Num1 = input('Enter the first number ')

if Num1.isdigit():
    Num2 = input('Enter the second number ')
    if Num2.isdigit():
        if int(Num1) > int(Num2):
            print(Num1, 'is the biggest number', end='\n')
            print('Summ: ', int(Num1)+int(Num2))
        else:
            print(Num2, 'is the biggest number')
            print('Summ: ', int(Num1)+int(Num2))
    else:
        print(Num2+str(pi))
else:
    print(Num1+str(pi))

