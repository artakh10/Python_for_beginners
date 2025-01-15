'''
Soecifically for python beginners
Author: Arta Khosravi
Last edit: Jan. 2025
'''

class AvgCalculator: #Camel Case
   n1_cr = 3
   n2_cr = 4
   n3_cr = 2 
   def calculate(self, n1,n2,n3): 
        #self is used because n1_cr was defined outside-
        #-the function
        #self is basically an adressor
        sum = n1*self.n1_cr + n2*self.n2_cr + n3*self.n3_cr
        average = sum / (self.n1_cr + 
                         self.n2_cr + self.n3_cr)
        return average