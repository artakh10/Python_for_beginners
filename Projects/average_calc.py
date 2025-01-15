'''
Soecifically for python beginners
Author: Arta Khosravi
Last edit: Jan. 2025
'''
# #initially
# n1 = float(input('Please enter your first score: '))
# n2 = float(input('Please enter your second score: '))
# n3 = float(input('Please enter your third score: '))
# n1_cr = 3
# n2_cr = 4
# n3_cr = 2
# sum = n1*n1_cr + n2*n2_cr + n3*n3_cr
# average = sum / (n1_cr + n2_cr + n3_cr)

#A Module (similar to NumPy)
from calc_class import *
inp_1 = float(input('Please enter your first score: '))
inp_2 = float(input('Please enter your second score: '))
inp_3 = float(input('Please enter your third score: '))
avg_calc_class = AvgCalculator()
avg = avg_calc_class.calculate(inp_1,inp_2,inp_3)
print(avg)