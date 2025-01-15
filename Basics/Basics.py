'''
Specifically for python beginners
Author: Arta Khosravi
Last edit: Jan. 2025
'''
pr_int = print(5); #pring a int
pr_fl = print (2.5); #print a float
pr_str = print('hello world'); #print a string

# variables
i = 5;j = 100; #variables
k = i+j; # s=i*j #operators 
print(type(i)) #<class 'int'>

list = [10,9,12,'string'] #list
print(type(list)) #<class 'list'>
print(list[len(list)])
length = list[0:len(list)+1]
print(length)


i = input('Enter a number:')
j = 8
k = int(i)
print('type i =',type(i),'type j =',type(j),'type k =',type(k))

#-------------#

# conditions/booleans
x = 4
i = (x <= 2)
print(i),print(x >= 2),print(x == 2)

#example 1
x=5
y='Name'
if (x==4 and y=='Name') or x < 1:
    print('Either x is lower than 1, or x is 4 And y is called Name.')
elif x==4 or y=='name':
    print('Somewhat, either x is 4, or y is not named /Name/')
elif not ((x==4 and y=='Name') or x > 1):
    print('Nope!')
else:
    i = input('None of the conditions are true, ' 
              'enter another number: ')
    j = input('And enter a string: ')
    if int(i) == 4 and j == 'string':
        print('You have done it!')

#example 2
x=2
y='Name'
if True:
    print('Yep, x is 4 And y is called Name')
elif False:
    print('Nope!')

#an example for conditions:
##simple calculator
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

##simplified calculator
i = int(input('Please enter a number: '))
j = int(input('Please enter another number: '))
k = input('Please enter an operator (+,-,*,/): ')
valid_operators = {'+': i+j, '-': i-j, '*': i*j,'/':i/j} # A SET
if k in valid_operators:
    print('{} {} {} = {}'.format(i, k, j, valid_operators[k]))

#---------------------------#

#loops:

# for loop:
import numpy as np
list = [1,2,3,4,5,6]
for l in list:
    if l > np.mean(list):
        print(l)
print('Done!')

# while loop:
i = 4
while i <= 5:
    print(i) #if put here, it prints first i , then i + 1
    i = i + 1
    #print(i) #if put here, it prints first i + 1 only
print('Done')

#an example for while loops using functions:
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

#an example for while and conditions:
#a sum function using while
total = 0
print('This is a sum calculator!')
while True:
    num = input('Please enter a number (comment STOP to calculate): ')
    if num.upper() == 'STOP': #.upper gives all the strings a caps lock
        break #stop the loop and calculate
    total += float(num) #add each given number to the previous one
    #and append them all to the 'total' variable
    #basically a sum function
print(total)

#an example for while and conditions
#give out sum of numbers
i= 0
sum = 0
count = 0
#While i != '' ##if you want your loop to break if you put null
while True:
    i = input('Enter your number: ')
    if i == '':
        ans=input('You didnt enter a number! Want to try again? ')
        if ans.lower() == 'yes':
            continue  #Start over to the beginning of the loop
        else:
            break
    i = float(i)
    i += i #adds the number to itself
    sum += i # sum = sum + i
    count += 1 #count = count + 1
    # equals to i = i + i
    print(i,sum,count,count/sum)

#---------------------------#
# functions

# initial loop:
costumers = ['2','3','4']
i = input('n')
if i in costumers:
    print('Yes')
else:
    print('No')

#with function:

def search_cost(x):
    costumers = ['2','3','4']
    if x in costumers:
        return True
    else:
        return False

i = input('Enter a number: ')
result = search_cost(i)
if result:
    print('Yes')
else:
    print('No')

#---------------------------#
#Class (Object Oriented Programming basics):

class Students: #everything defined under/in class
    name = 'arta' # the name of the student
    def score(self,x,y,z): 
    #self always included as the first-
    # -parameter of the functions under class
    # x , y , z : grades of 3 lessons
        s = (x + y + z) / 3 #mean of the 3 lessons
        return s

myStudent = Students() #example 
#drops the class' info inside myStudent
#we can have access to the objs inside the class
result_st = myStudent.name #here prints 'arta
myStudent.name = 'Amin'
result_st = myStudent.name #here prints 'Amin'
print(result_st) #Name
print(myStudent.score(12,19,20)) #Score

## new parameter:
myStudent_2 = Students()
myStudent_2.name = 'Aram'
print(myStudent_2.name)
result_st = myStudent_2.score(14,20,10)
print(result_st)


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
