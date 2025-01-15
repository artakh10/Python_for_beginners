
'''
Soecifically for python beginners
Author: Arta Khosravi
Last edit: Jan. 2025
'''
### Calculator in class:
class Calculator:
    def calculate(self):
        x = float(input('Enter a number: '))
        y = float(input('Enter a second number: '))
        op = input('Enter an operation: ')
        valid_operators = {'+': x + y,'-': x - y,
                           '*': x * y,'/': x / y 
                           if y != 0 else 'Invalid'}
        if op in valid_operators:
            result = valid_operators[op]
            print('{} {} {} = {}'.format(x, op, y, result))
            return result
        else:
            print('Invalid operation')
            return None
calculator = Calculator()
calculator.calculate()