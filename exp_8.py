#  WAP for division of two numbers where denominator is 0. This will throw an exception. Now handle the exception using try and except.

try:
    num1 = float(input('first number: '))
    num2 = float(input('second number: '))
    print(num1/num2)
except ZeroDivisionError:
    print('num2 is 0')
except ValueError:
    print('num1 or num2 is not int')
else:
    print('Successful')
finally:
    print('Done')