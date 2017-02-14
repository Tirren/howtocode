from math import pi

def itsfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

Num1 = input('Enter the first number ')

if itsfloat(Num1):

    Num2 = input('Enter the second number ')

    if itsfloat(Num2):
        if float(Num1) > float(Num2):
            print(Num1, 'is the biggest number')
            print('Summ:', float(Num1)+float(Num2))
        else:
            print(Num2, 'is the biggest nubmer')
            print('Summ:', float(Num1)+float(Num2))
    else:
        print(Num2+str(pi))
else:
        print(Num1+str(pi))
