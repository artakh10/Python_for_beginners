'''
Soecifically for python beginners
Author: Arta Khosravi
Last edit: Jan. 2025
'''
# #method 1: using while
# while True:
#     inp = str(input('Please enter a sentence: '))
#     try:
#         list_inp = inp.split() #split the string into words
#         fin_list = []
#         for i in range(len(list_inp)):
#             if list_inp[i][0].isupper() == True: #check if the first word is capitalized
#                 new_list=list_inp[i][0] #first letter of every list element/word
#                 fin_list.append(new_list)
#         fin_ac = ""
#         fin_ac = fin_ac.join(fin_list) #combine the list elements into a single string
#         print('Your acronym is: ',fin_ac)
#         ans = str(input('Do you want to try again? (y/n): '))
#         if  ans =='n':
#             break 
#     except ValueError:
#         print('Incorrect. Enter a String.')
#         break

#method 2 : using class / def :
class Acronym:
    def __init__(self): #__init__ is the initial description
        #usually mandatory for the class to run
        self.inp = input('Please enter a sentence: ')
    def acronym(self):
            list_inp = self.inp.split() #split the string into words
            fin_list = []
            for i in range(len(list_inp)):
                if list_inp[i][0].isupper() == True: #check if the first word is capitalized
                    new_list=list_inp[i][0] #first letter of every list element/word
                    fin_list.append(new_list)
            fin_ac = ""
            fin_ac = fin_ac.join(fin_list) #combine the list elements into a single string
            print('Your acronym is: ',fin_ac)
            return fin_ac
acronym_instance = Acronym()
acronym_instance.acronym()