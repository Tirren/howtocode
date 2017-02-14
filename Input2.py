from math import pi

Num1 = input('Enter the first number ')

try:
    if float(Num1):
        Num2 = input('Enter the second number ')
        try:
            if float(Num2):
                if float(Num1) > float(Num2):
                    print(Num1, 'is a biggest nubmer')
                    print(float(Num1) + float(Num2))
                else:
                    print(Num2, 'is a biggest number')
                    print(float(Num1) + float(Num2))
        except ValueError:
            print(Num2+str(pi))
except ValueError:
 print(Num1+str(pi))
