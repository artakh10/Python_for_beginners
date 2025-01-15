'''
Soecifically for python beginners
Author: Arta Khosravi
Last edit: Jan. 2025
'''

##simple calculator using only if
i = int(input('Please enter a number: '))
j = int(input('Please enter another number: '))
k = input('Please enter an operator (+,-,*,/): ')
if k == '+':
    print((i)+(j))
elif k == '-':
    print((i)-(j))
elif k == '*':
    print((i)*(j))
elif k == '/' and j != 0:
    print((i)/(j))
else:
    print('Error')

##simplified calculator using a dictionary
i = int(input('Please enter a number: '))
j = int(input('Please enter another number: '))
k = input('Please enter an operator (+,-,*,/): ')
valid_operators = {'+': i+j, '-': i-j, '*': i*j,'/':i/j} # A SET
if k in valid_operators:
    print('{} {} {} = {}'.format(i, k, j, valid_operators[k]))