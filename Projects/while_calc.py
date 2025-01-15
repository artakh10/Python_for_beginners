'''
Soecifically for python beginners
Author: Arta Khosravi
Last edit: Jan. 2025
'''

# Calculator using While:
i = False
while True:
    def eq(i,j,k): #a function with parameters being i, j and k
        return int(i)+(int(j))+(int(k))
    i = input('Please enter a number (comment STOP to stop): ')
    j = input('Please enter a second number: ')
    k = input('Please enter a third number: ')
    print('{} + {} + {} = {}'.format(i, j,k,eq(i,j,k))) #format replaces the parameters inside the printed string
    if i == 'STOP':
        break