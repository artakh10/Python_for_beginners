'''
Soecifically for python beginners
Author: Arta Khosravi
Last edit: Jan. 2025
'''
import os
__DIR__ = os.path.dirname(os.path.abspath(__file__))
months = {
    '1':'aries','2':'taurus',
    '3':'gemini','4':'cancer','5':'leo','6':'virgo',
    '7':'libra','8':'scorpio','9':'sagittarius',
    '10':'capricorn','11':'aquarius','12':'pisces'
}
while True:
    i = input('Enter Your Birth Month (1-12): ')
    try:
        file = open(__DIR__+ '\\'+ str(months[i]) + '.txt', 'r')
        m = file. read()
        print('Your fortune for your month, {}, is: {}'.format(months[i],m))
        ans = input('Wanna see the other months? (y/n)')
        if ans == 'n':
            break
    except ValueError:
        if int(i) < 1 or int(i) > 12:
            print("Your Number is not valid. Try again.")